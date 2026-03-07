<template>
  <div id="app-wrapper">
    <header class="navbar">
      <div class="container navbar-inner">
        <!-- Temporary div to balance flex space if needed -->
        <div class="burger-menu" @click="isSideMenuOpen = true">
          <!-- Placeholder for mobile menu burger -->
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 12H21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <path d="M3 6H21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <path d="M3 18H21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </div>

        <router-link to="/" class="logo-link">
          <img :src="'/images/designElementsImages/logo/logo.png'" alt="UMAI Logo" class="logo" />
        </router-link>

        <div class="nav-actions">
          <select v-model="$i18n.locale" class="lang-selector">
            <option value="en">eng</option>
            <option value="ru">рус</option>
            <option value="kk">қаз</option>
          </select>
        </div>
      </div>
    </header>

    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- Side Menu Overlay & Drawer -->
    <transition name="fade">
      <div v-if="isSideMenuOpen" class="side-menu-overlay" @click="isSideMenuOpen = false"></div>
    </transition>
    
    <transition name="slide-left">
      <nav v-if="isSideMenuOpen" class="side-menu-drawer">
        <div class="drawer-header">
           <img :src="'/images/designElementsImages/logo/logo.png'" alt="UMAI Logo" class="logo-drawer" />
           <button class="close-btn" @click="isSideMenuOpen = false">
             <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
               <path d="M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
               <path d="M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
             </svg>
           </button>
        </div>
        <div class="drawer-links">
           <router-link to="/" class="drawer-link" @click="isSideMenuOpen = false">{{ $t('nav.home') }}</router-link>
           <router-link to="/menu" class="drawer-link" @click="isSideMenuOpen = false">{{ $t('nav.menu') }}</router-link>
           
           <div class="drawer-divider"></div>
           
           <a href="https://wa.me/" target="_blank" class="drawer-link social">{{ $t('nav.whatsapp') }}</a>
           <a href="https://instagram.com/" target="_blank" class="drawer-link social">{{ $t('nav.instagram') }}</a>
        </div>
      </nav>
    </transition>

    <!-- Floating Cart Button -->
    <transition name="slide-up">
      <div v-if="cartItemCount > 0 && $route.name !== 'cart'" class="floating-cart-wrapper">
        <router-link to="/cart" class="floating-cart-btn">
          <div class="cart-info">
            <span class="cart-count">{{ cartItemCount }}</span>
            <span class="cart-label">{{ $t('nav.cart') }}</span>
          </div>
          <span class="cart-total">{{ cartTotal }}tg</span>
        </router-link>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { cartItemCount, cartTotal } from './store/cart'
import { useRoute } from 'vue-router'

const route = useRoute()
const isSideMenuOpen = ref(false)
</script>

<style scoped>
.navbar {
  background-color: var(--color-bg);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

.navbar-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.burger-menu {
  color: var(--color-accent);
  cursor: pointer;
}

.logo-link {
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo {
  height: 48px;
  object-fit: contain;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.lang-selector {
  background: transparent;
  border: none;
  font-family: inherit;
  font-size: 1rem;
  font-weight: 500;
  color: var(--color-text-main);
  cursor: pointer;
  outline: none;
  text-transform: lowercase;
}

.main-content {
  flex: 1;
  padding-bottom: 80px; /* Space for the floating button */
}

/* Floating Cart Styles */
.floating-cart-wrapper {
  position: fixed;
  bottom: 24px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  pointer-events: none; /* Let clicks pass through the invisible wrapper */
  z-index: 1000;
  padding: 0 1rem;
}

.floating-cart-btn {
  pointer-events: auto; /* Re-enable clicks on the button itself */
  background-color: var(--color-accent);
  color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  max-width: 400px;
  padding: 12px 20px;
  border-radius: 100px;
  box-shadow: 0 8px 24px rgba(196, 164, 106, 0.4);
  backdrop-filter: blur(10px);
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
}

.floating-cart-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(196, 164, 106, 0.5);
  color: var(--color-white);
}

.cart-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.cart-count {
  background-color: var(--color-white);
  color: var(--color-accent);
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
}

.cart-label {
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.cart-total {
  font-weight: 600;
  font-size: 1.1rem;
}

.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.slide-up-enter-from,
.slide-up-leave-to {
  opacity: 0;
  transform: translateY(100px);
}

/* Side Menu Styles */
.side-menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(2px);
  z-index: 200;
}

.side-menu-drawer {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 280px;
  background-color: var(--color-bg);
  background-image: url('/images/designElementsImages/Слой 1.png'); /* Add slight texture */
  background-size: 200px;
  background-position: bottom left;
  background-repeat: no-repeat;
  z-index: 201;
  box-shadow: 4px 0 24px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  padding: 1.5rem;
}

.drawer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 3rem;
}

.logo-drawer {
  height: 40px;
  object-fit: contain;
}

.close-btn {
  background: rgba(196, 164, 106, 0.1);
  border-radius: 50%;
  border: none;
  color: var(--color-accent);
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}

.close-btn:hover {
  background: rgba(196, 164, 106, 0.2);
}

.drawer-links {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.drawer-link {
  font-family: var(--font-header);
  font-size: 1.8rem;
  color: var(--color-text-main);
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  transition: var(--transition);
}

.drawer-link:hover {
  color: var(--color-accent);
  transform: translateX(5px);
}

.drawer-divider {
  height: 1px;
  background-color: rgba(196, 164, 106, 0.2);
  margin: 1.5rem 0;
}

.social {
  font-family: var(--font-main);
  font-size: 1.1rem;
  text-transform: none;
  letter-spacing: 0;
  display: flex;
  align-items: center;
}

.social::before {
  content: '→';
  color: var(--color-accent);
  margin-right: 8px;
  transition: var(--transition);
}

.social:hover::before {
  transform: translateX(4px);
}

/* Transitions */
.slide-left-enter-active,
.slide-left-leave-active {
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.slide-left-enter-from,
.slide-left-leave-to {
  transform: translateX(-100%);
}
</style>
