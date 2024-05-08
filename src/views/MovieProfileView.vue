
<template>
    <div class="movies-container">
        <h1>Movies</h1>

        <div class="movies">
            <div v-for="movie in movies" class="movie">
                <div class="poster-container">
                    <img :src="getPosterUrl(movie.poster)" class="movie-poster" :alt="movie.title"/>
                </div>
                <div class="movie-details">
                    <h2>{{movie.title }}</h2>
                    <p>{{ movie.description }}</p>
                </div>
                
            </div>
        </div>

    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

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
      /*console.error('Error fetching movies:', error);*/
    }
});

 //method to construct the poster URL
 function getPosterUrl(filename) {
    return `/api/v1/posters/${filename}`;
 }


</script>

<style>

form {
    display: flex;
    flex-direction: column;
  }

    .movies-container{
        margin: auto 100px;
    }

    .movies{
        display: flex;
        flex-wrap: wrap;
    }
    .movie{
        max-width: 550px;
        height: 250px;
        width: 100%;
        overflow: hidden;

        display: grid;
        grid-template-columns: 1fr 2fr;

        margin: 20px;
        border-radius: 5px;
        box-shadow: 0 0 5px rgb(209, 209, 209);
    }
    .movie img{
        width: 100%;
        height: 250px;
        object-fit: contain;
    }
    .movie-details{
        padding: 15px;
    }
</style>