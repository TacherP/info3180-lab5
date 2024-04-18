<template>
  <div class="container">
    <h1>Movies</h1>
    <div v-if="movies.length === 0" class="no-movies">No movies available</div>
    <div v-else class="viewing-title">
      <div v-for="movie in movies" :key="movie.id" class="movie-view">
        <a :href="movie.poster" target="_blank" class="movie-card">
          <img :src="getPosterUrl (movie.poster)" :alt="movie.title" class="movie-poster" />
        </a>
        <div class="movie-details">
          <h3 class="details-title">{{ movie.title }}</h3>
          <p class="details-description">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let movies = ref([]);

  onMounted(async () => {
    try {
      const response = await fetch('/api/v1/movies');
      if (!response.ok) {
        throw new Error ("Failed to fetch movies");
      }
      const data = await response.json();
      movies.value = data.movies;
    } catch (error) {
      console.error('Error fetching movies:', error);
    }
  });

  //method to construct the poster URL
  function getPosterUrl(filename) {
    return `/api/v1/posters/${filename}`;
  }

</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 20px;
}

.gallery-item {
  background-color: #f1f1f1;
  border-radius: 4px;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.gallery-item:hover {
  transform: scale(1.05);
}

.gallery-link {
  display: block;
}

.gallery-image {
  width: 100%;
  height: 400px;
  object-fit: cover;
}

.gallery-info {
  padding: 15px;
}

.gallery-title {
  margin-top: 0;
  margin-bottom: 5px;
  font-size: 1.2rem;
}

.gallery-description {
  margin: 0;
  font-size: 0.9rem;
  color: #666;
}

.no-movies {
  text-align: center;
  font-size: 1.2rem;
  color: #888;
  margin-top: 40px;
}
</style>