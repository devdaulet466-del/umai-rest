<template>
  <div class="home container mt-8">
    <div class="hero text-center">
      <h1>{{ $t('home.welcome') }}</h1>
      <p class="subtitle mb-8">{{ $t('home.subtitle') }}</p>
      
      <div class="showcase">
        <!-- Using a placeholder promo image from assets -->
        <img :src="'/images/foodImages/IMG_1469.JPG'" alt="Showcase" class="hero-image" />
      </div>

      <router-link to="/menu" class="btn mt-8">
        {{ $t('home.cta') }}
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.hero {
  padding: 2rem 0;
}

.subtitle {
  font-size: 1.25rem;
  color: #666;
}

.showcase {
  max-width: 600px;
  margin: 0 auto;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.hero-image {
  width: 100%;
  height: auto;
  aspect-ratio: 4/3;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.hero-image:hover {
  transform: scale(1.05);
}
</style>
