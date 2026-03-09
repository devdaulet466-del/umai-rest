<template>
  <div class="menu container mt-4">
    <div class="search-bar mb-4">
      <div class="search-input-group">
        <input type="text" :placeholder="$t('menu.search')" class="search-input" />
        <button class="btn btn-search">{{ $t('menu.search_btn') }}</button>
      </div>
    </div>

    <div v-if="loading" class="text-center mt-8">Loading menu...</div>
    <div v-else>
      <!-- Special Menu Section -->
      <section v-if="specialMenu" class="special-menu-section mb-8">
        <h2 class="category-title">{{ specialMenu.name[$i18n.locale] }}</h2>
        <div class="special-menu-scroll">
          <div v-for="item in specialMenu.items" :key="item.id" class="menu-card special-card" @click="openModal(item)">
            <div class="img-wrapper">
              <img :src="`/${item.image}`" :alt="item.name[$i18n.locale]" />
            </div>
            <div class="card-content mt-4">
              <h3 class="item-name">{{ item.name[$i18n.locale] }}</h3>
              <p v-if="item.description" class="item-desc">{{ item.description[$i18n.locale] }}</p>
              
              <div class="card-footer mt-4">
                <span class="price">{{ item.price }}tg</span>
                <button @click.stop="addToCart(item)" class="btn-add">
                  {{ $t('menu.add_to_cart') }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Sticky Category Tabs -->
      <div class="category-tabs-wrapper sticky-tabs mb-8">
        <div class="category-tabs">
          <button 
            class="tab-btn" 
            :class="{ active: selectedCategory === 'all' }"
            @click="selectedCategory = 'all'"
          >
            {{ $t('menu.all_categories') }}
          </button>
          <button 
            v-for="(cat, index) in categories" 
            :key="cat.id" 
            class="tab-btn"
            :class="{ active: selectedCategory === cat.id }"
            @click="selectedCategory = cat.id"
          >
            {{ cat.name[$i18n.locale] }}
          </button>
        </div>
      </div>

      <!-- Subcategories of the selected category -->
      <div v-for="cat in displayedCategories" :key="cat.id">
        <!-- Optional: Show Category Title if ALL is selected to separate them visually -->
        <h2 v-if="selectedCategory === 'all'" class="category-title mt-8 mb-4" style="text-align: left; font-size: 2rem;">{{ cat.name[$i18n.locale] }}</h2>
        
        <section v-for="sub in cat.subcategories" :key="sub.id" class="subcategory-section mb-8">
          <h3 class="subcategory-title">{{ sub.name[$i18n.locale] }}</h3>
          
          <div class="menu-grid mt-4">
            <div v-for="item in sub.items" :key="item.id" class="menu-card" @click="openModal(item)">
              <div class="img-wrapper">
                <img :src="`/${item.image}`" :alt="item.name[$i18n.locale]" />
              </div>
              <div class="card-content mt-4">
                <h4 class="item-name">{{ item.name[$i18n.locale] }}</h4>
                <p v-if="item.description" class="item-desc">{{ item.description[$i18n.locale] }}</p>
                
                <div class="card-footer mt-4">
                  <span class="price">{{ item.price }}tg</span>
                  <button @click.stop="addToCart(item)" class="btn-add">
                    {{ $t('menu.add_to_cart') }}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>

    <!-- Dish Modal -->
    <transition name="modal-slide">
      <div v-if="selectedDish" class="dish-modal-overlay" @click="closeModal">
        <div class="dish-modal-content" @click.stop>
          <button class="modal-close" @click="closeModal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
              <path d="M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
          
          <div class="modal-img-wrapper">
            <img :src="`/${selectedDish.image}`" :alt="selectedDish.name[$i18n.locale]" />
          </div>
          
          <div class="modal-body">
            <h2 class="modal-title">{{ selectedDish.name[$i18n.locale] }}</h2>
            <p v-if="selectedDish.weight" class="modal-weight">{{ selectedDish.weight }}</p>
            <p v-if="selectedDish.description" class="modal-desc">{{ selectedDish.description[$i18n.locale] }}</p>

            <div v-if="selectedDish.ingredients" class="modal-ingredients-wrapper">
              <h4 class="modal-ingredients-title">{{ $t('menu.ingredients') }}:</h4>
              <p class="modal-ingredients">{{ selectedDish.ingredients[$i18n.locale] }}</p>
            </div>
            
            <div class="modal-footer">
              <span class="modal-price">{{ selectedDish.price }}tg</span>
              <button @click="addToCart(selectedDish); closeModal()" class="btn-add modal-btn-add">
                {{ $t('menu.add_to_cart') }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { addToCart } from '../store/cart'

const categories = ref([])
const specialMenu = ref(null)
const loading = ref(true)
const selectedCategory = ref('all')
const selectedDish = ref(null)

const openModal = (item) => {
  selectedDish.value = item
  document.body.style.overflow = 'hidden' // Prevent bg scrolling
}

const closeModal = () => {
  selectedDish.value = null
  document.body.style.overflow = ''
}

const displayedCategories = computed(() => {
  if (selectedCategory.value === 'all') {
    return categories.value
  }
  const activeCat = categories.value.find(c => c.id === selectedCategory.value)
  return activeCat ? [activeCat] : []
})

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:8000/api/menu')
    const data = await response.json()
    categories.value = data.categories
    specialMenu.value = data.special_menu
    
    // Auto-select first category (or all)
    if (categories.value.length > 0 && selectedCategory.value === '') {
      selectedCategory.value = 'all'
    }
  } catch (error) {
    console.error("Failed to load menu", error)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.search-input-group {
  display: flex;
  gap: 0.5rem;
}

.search-input {
  flex: 1;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  border: 1px solid rgba(0,0,0,0.1);
  background-color: var(--color-secondary-bg);
  font-family: inherit;
  font-size: 1rem;
  color: var(--color-text-main);
  outline: none;
  transition: var(--transition);
}

.search-input:focus {
  border-color: var(--color-accent);
}

.btn-search {
  border-radius: 12px;
  padding: 0 1.5rem;
}

/* Category Tabs */
.sticky-tabs {
  position: sticky;
  top: 70px; /* Adjust based on your navbar height */
  z-index: 90;
  background-color: var(--color-bg); /* Match background so it overlays content */
  padding-top: 1rem;
  margin-top: -1rem;
  border-bottom: 1px solid rgba(196, 164, 106, 0.2);
}

.category-tabs-wrapper {
  margin-left: -1rem;
  margin-right: -1rem;
  padding: 0.5rem 1rem 0 1rem;
}

.category-tabs {
  display: flex;
  overflow-x: auto;
  gap: 1.5rem;
  padding-bottom: 0.5rem;
  padding-top: 1rem;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none;  /* Internet Explorer 10+ */
}

.category-tabs::-webkit-scrollbar { 
  display: none; /* WebKit */
}

.tab-btn {
  white-space: nowrap;
  padding: 0.5rem 0;
  border: none;
  background: transparent;
  color: #a09d98;
  font-family: var(--font-header);
  font-weight: 500;
  font-size: 1.4rem;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  cursor: pointer;
  transition: var(--transition);
  position: relative;
}

.tab-btn:hover {
  color: var(--color-accent);
}

.tab-btn.active {
  color: var(--color-accent);
  font-weight: 600;
}

.category-title {
  font-size: 1.8rem;
  /*text-align: center;
  margin-bottom: 1.5rem; */
}

.subcategory-title {
  font-size: 1.3rem;
  border-bottom: 1px solid rgba(196, 164, 106, 0.2);
  padding-bottom: 0.5rem;
  margin-top: 2rem;
}

.special-card {
  border: 2px solid rgba(196, 164, 106, 0.3);
  box-shadow: 0 8px 24px rgba(196, 164, 106, 0.1);
  min-width: 280px; /* Fixed width for carousel items */
  width: 340px; 
  flex: 0 0 auto;
}

.special-menu-scroll {
  display: flex;
  overflow-x: auto;
  gap: 1.5rem;
  padding: 1rem 1rem 1.5rem 1rem;
  margin: 0 -1rem;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* Internet Explorer 10+ */
}

.special-menu-scroll::-webkit-scrollbar {
  display: none; /* WebKit */
}

.menu-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 768px) {
  .menu-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .menu-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.menu-card {
  background: var(--color-white);
  border-radius: 16px;
  padding: 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  display: flex;
  flex-direction: column;
  transition: var(--transition);
  cursor: pointer;
}

.menu-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
}

.img-wrapper {
  overflow: hidden;
  border-radius: 12px;
  height: 200px;
}

.img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.menu-card:hover .img-wrapper img {
  transform: scale(1.05);
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.item-name {
  font-size: 1.4rem;
  color: var(--color-text-main);
  text-transform: none;
}

.item-desc {
  font-size: 0.9rem;
  color: #888;
  margin-top: 0.5rem;
  flex: 1;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--color-accent);
}

.btn-add {
  display: none;
  background: transparent;
  color: var(--color-accent);
  border: 1px solid var(--color-accent);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}

.btn-add:hover {
  background: var(--color-accent);
  color: var(--color-white);
}

/* Dish Modal */
.dish-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: flex-end; /* Align to bottom */
  padding: 0; /* Remove padding */
}

.dish-modal-content {
  background: var(--color-bg);
  background-image: url('/images/designElementsImages/Слой 1.png');
  background-size: 150px;
  background-position: bottom right;
  background-repeat: no-repeat;
  border-radius: 20px 20px 0 0; /* Round top corners only */
  width: 100%;
  max-width: 600px;
  max-height: 90vh;
  position: relative;
  overflow-y: auto;
  box-shadow: 0 -8px 32px rgba(0,0,0,0.2);
  display: flex;
  flex-direction: column;
}

.modal-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(4px);
  border: none;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-main);
  cursor: pointer;
  z-index: 2;
  transition: var(--transition);
}

.modal-close:hover {
  background: var(--color-white);
  color: var(--color-accent);
}

.modal-img-wrapper {
  width: 100%;
  height: 250px;
}

.modal-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.modal-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.modal-title {
  font-family: var(--font-header);
  font-size: 2rem;
  color: var(--color-text-main);
  margin-bottom: 0.5rem;
  line-height: 1.2;
}

.modal-weight {
  font-size: 0.9rem;
  color: var(--color-text-main);
  opacity: 0.6;
  margin-bottom: 1rem;
}

.modal-desc {
  font-size: 1.05rem;
  color: var(--color-text-main);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.modal-ingredients-wrapper {
  margin-bottom: 2rem;
}

.modal-ingredients-title {
  font-family: var(--font-header);
  font-size: 1.2rem;
  color: var(--color-accent);
  margin-bottom: 0.25rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.modal-ingredients {
  font-size: 0.95rem;
  color: var(--color-text-main);
  line-height: 1.5;
  opacity: 0.8;
}

.modal-footer {
  margin-top: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid rgba(196, 164, 106, 0.2);
  padding-top: 1rem;
}

.modal-price {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--color-accent);
}

.modal-btn-add {
  padding: 0.75rem 2rem;
  font-size: 1.1rem;
}

/* Modal Transitions */
.modal-slide-enter-active,
.modal-slide-leave-active {
  transition: opacity 0.3s ease;
}

.modal-slide-enter-from,
.modal-slide-leave-to {
  opacity: 0;
}

.modal-slide-enter-active .dish-modal-content,
.modal-slide-leave-active .dish-modal-content {
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1);
}

.modal-slide-enter-from .dish-modal-content,
.modal-slide-leave-to .dish-modal-content {
  transform: translateY(100%);
}
</style>
