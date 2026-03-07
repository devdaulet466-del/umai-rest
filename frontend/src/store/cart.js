import { reactive, computed } from 'vue'

export const cartState = reactive({
    items: []
})

export function addToCart(product) {
    const existingItem = cartState.items.find(item => item.id === product.id)
    if (existingItem) {
        existingItem.quantity++
    } else {
        cartState.items.push({ ...product, quantity: 1 })
    }
}

export function removeFromCart(productId) {
    const index = cartState.items.findIndex(item => item.id === productId)
    if (index !== -1) {
        cartState.items.splice(index, 1)
    }
}

export function updateQuantity(productId, quantity) {
    const item = cartState.items.find(item => item.id === productId)
    if (item) {
        if (quantity <= 0) {
            removeFromCart(productId)
        } else {
            item.quantity = quantity
        }
    }
}

export function clearCart() {
    cartState.items = []
}

export const cartTotal = computed(() => {
    return cartState.items.reduce((total, item) => total + (item.price * item.quantity), 0)
})

export const cartItemCount = computed(() => {
    return cartState.items.reduce((count, item) => count + item.quantity, 0)
})
