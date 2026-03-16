<template>
  <div class="cart container mt-8">
    <h1 class="text-center">{{ $t('cart.title') }}</h1>
    
    <div v-if="successMsg" class="success-alert mb-8 mt-4 text-center">
      {{ successMsg }}
    </div>

    <div v-if="cartState.items.length === 0" class="text-center mt-8 empty-cart">
      <p>{{ $t('cart.empty') }}</p>
      <router-link to="/menu" class="btn mt-4">Go to Menu</router-link>
    </div>

    <div v-else class="cart-content mt-8">
      <div class="cart-items">
        <div v-for="item in cartState.items" :key="item.id" class="cart-item">
          <div class="item-info">
            <h4>{{ item.name[$i18n.locale] }}</h4>
            <p>{{ item.price }}tg</p>
          </div>
          <div class="item-actions">
            <button class="qty-btn" @click="updateQuantity(item.id, item.quantity - 1)">-</button>
            <span class="qty">{{ item.quantity }}</span>
            <button class="qty-btn" @click="updateQuantity(item.id, item.quantity + 1)">+</button>
          </div>
        </div>
      </div>

      <div class="cart-summary mt-8">
        <div class="summary-row">
          <span>{{ $t('cart.total') }}:</span>
          <span class="total-price">{{ cartTotal }}tg</span>
        </div>
        
        <button @click="submitCheckout" class="btn checkout-btn mt-4" :disabled="loading">
          {{ loading ? '...' : $t('cart.checkout') }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { cartState, cartTotal, updateQuantity, clearCart } from '../store/cart'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const loading = ref(false)
const successMsg = ref('')

async function submitCheckout() {
  loading.value = true
  try {
    const payload = {
      items: cartState.items.map(i => ({ id: i.id, quantity: i.quantity })),
      total_price: cartTotal.value,
      comment: "Frontend checkout"
    }
    const res = await fetch('https://umai-rest-backend.onrender.com/api/checkout', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    
    if (res.ok) {
      clearCart()
      successMsg.value = t('cart.success')
      setTimeout(() => successMsg.value = '', 5000)
    }
  } catch (error) {
    console.error("Checkout failed:", error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.cart-content {
  max-width: 600px;
  margin: 0 auto;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

.item-info h4 {
  margin-bottom: 0.25rem;
  color: var(--color-text-main);
  text-transform: none;
}

.item-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.qty-btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1px solid var(--color-accent);
  background: white;
  color: var(--color-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  cursor: pointer;
  transition: var(--transition);
}

.qty-btn:hover {
  background: var(--color-accent);
  color: white;
}

.qty {
  font-weight: 600;
  min-width: 20px;
  text-align: center;
}

.cart-summary {
  background: var(--color-white);
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.03);
}

.summary-row {
  display: flex;
  justify-content: space-between;
  font-size: 1.25rem;
  font-weight: 600;
}

.total-price {
  color: var(--color-accent);
}

.checkout-btn {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
}

.success-alert {
  background-color: #d4edda;
  color: #155724;
  padding: 1rem;
  border-radius: 8px;
  font-weight: 500;
}

.empty-cart {
  color: #888;
}
</style>
