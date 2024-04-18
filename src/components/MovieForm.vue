
<template>

  <form @submit.prevent="saveMovie" id="movieform">
      <h1>Add Movie</h1>
      <hr>
      <div class="form-group mb-3">
          <label for="title" class="form-label">Title</label>
          <input type="text" name="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
          <label for="description" class="form-label">Description</label>
          <textarea name="description" class="form-control" ></textarea>
      </div>

      <div class="form-group mb-3">
          <label for="poster" class="form-label">Poster</label>
          <input type="file" name="poster" class="form-control" accept=".jpg,.png.jpeg" />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
      <div v-if="successMessage" class="message success"> {{ successMessage }} </div>
      <div v-if="errorMessage.length > 0" class="message error">
        <ul>
          <li v-for="(message, index) in errorMessage" :key="index"> {{ message }}</li>
        </ul>
      </div>

    </form>

</template>

<script setup>

  import {ref, onMounted} from "vue";
  let csrf_token = ref("");
  const successMessage = ref("");
  const errorMessage = ref([]);
  const formData = ref ({
    title: '',
    description: '',
    poster: null
  })
 
  function getCsrfToken() {
    fetch('/api/v1/csrf-token')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        csrf_token.value = data.csrf_token;
      })
      .catch(error => {
        console.error('Error fetching CSRF token:', error);
      });
  }

  // Call getCsrfToken when the component is mounted
  onMounted(() => {
    getCsrfToken();
  });

  // Function to handle file change
  function handleFileChange(event) {
    formData.poster = event.target.files[0];
  }

  // Function to handle form submission
function saveMovie() 
{

    let movieForm = document.getElementById('movieForm');
    let form_data = new formData(movieForm);

    form_data.append('title', formData.title);
    form_data.append('description', formData.description);
    form_data.append('poster', formData.poster);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
        'X-CSRFToken': csrf_token.value
        }
    })
    .then(function (response) {
        if (!response.ok) {
          
          throw new Error('Network response was not ok'); 

        }
        return response.json();
    })
    .then(function (data) {
        console.log(data);

        // Clear the form data after successful submission
        formData.value = {
            title: '',
            description: ''
        };
        
        // Clear the form data after successful submission, primarly uploads
        movieForm.reset(); // Reset the form
        
        // Clear success message
        successMessage.value = '';

        // Clear error message space before processing the form
        errorMessage.value = []; // Clear error message space before processing the form
    
              // Show success message
        successMessage.value = 'File Upload Successfully!';

    })
    .catch(function (error) {
        console.error('There was a problem with the fetch operation:', error);
        
        // Clear success message
        successMessage.value = '';

        // Clear error message space before processing the form
        errorMessage.value = []; 

        if (!formData.value.title.trim()) {
            errorMessage.value.push('Error in the Title field - This field is required.');
        }
        if (!formData.value.description.trim()) {
            errorMessage.value.push('Error in the Description field - This field is required.');
        }
        if (!formData.poster) {
            errorMessage.value.push('Error in the Photo field - This field is required.');
        }
    
    });

}
</script>
  
<style>
body {
  padding-top: 5rem;
  background-color: rgb(198, 228, 250);
  height: 100vh;
}

.form-label{
  font-weight: bold;
}

form{
  max-width: 900px;
  background-color: white;
  padding: 50px;
  border-radius: 5px;
  margin:0 auto;
  margin-top: 50px;
}
</style>