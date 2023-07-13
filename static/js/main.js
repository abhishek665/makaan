function setCityModal(){
    
}
function closeSearchContainerNav() {
    document.getElementsByClassName('search-container')[0].classList.remove('search-container-nav');
    $('#my-nav-container').css({'display': 'flex'});
    $('#close-search-container-nav').css({'display': 'none'});
    $('body').css({'overflow': 'scroll'})
}
function searchCarouselCloseBtn(){
  $('#search-carousel').css({'display': 'none'})
  document.getElementById('search').value = '';
  // $('#search-carousel').carousel('next');
}
function showCities(){
  $('#cities-modal').show();
}
function closeCitiesModal(){
  $('#cities-modal').hide();
}
$('.btn-tab').click(function () {
  ca = document.querySelector('[class="btn-tab btn active"]')
  ca.setAttribute('class', 'btn-tab btn');
  $(this).addClass('btn-tab btn active');
  document.getElementById('type').setAttribute('value', (this.id))
  console.log((this));
})
// Load the Google Maps Places library
function loadPlacesLibrary() {
const script = document.createElement('script');
script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyDP76BIL0N496OLE-av_KlsnA0Hsl00c5w&libraries=places";
script.defer = true;
document.head.appendChild(script);
}

// Initialize the Autocomplete functionality
function initializeAutocomplete() {
  if (window.innerWidth < 600){
      $('#my-nav-container').css({'display': 'none'});
      document.getElementsByClassName('search-container')[0].classList.add('search-container-nav');
      $('#close-search-container-nav').css({'display': 'inline-block'});
      window.scrollTo({
        top: 0,
        behavior: "smooth" // Optional: Add smooth scrolling animation
      });
      $('body').css({'overflow': 'hidden'})
    }
const input = document.getElementById('search');
const city = document.getElementById('h-city').getAttribute('value');
console.log('oiiiiiiiiiiiiiiiiiiiii', city)
const geocoder = new google.maps.Geocoder();
let latitude = 0
let longitude = 0
// Perform geocoding for the city
const geocodePromise = new Promise((resolve, reject) => {

  geocoder.geocode({ address: city }, (results, status) => {
    if (status === google.maps.GeocoderStatus.OK && results.length > 0) {
        // Get the latitude and longitude of the first result
      resolve(results[0].geometry.location);
    } else {
      reject(status);
    }
  }); 
});
geocodePromise
.then((location) => {
      latitude = location.lat();
      longitude = location.lng();

      // Use the latitude and longitude as needed
      console.log("Latitude:", latitude);
      console.log("Longitude:", longitude);
      let lucknowBounds = new google.maps.LatLngBounds(
      new google.maps.LatLng(latitude, longitude), // Southwest corner coordinates
      new google.maps.LatLng(latitude + 0.10, longitude + 0.10) // Northeast corner coordinates
    );
    console.log(latitude, longitude, 'hhhhhhhhhhhhhhhhhhhhhhhh');
    const autocomplete = new google.maps.places.Autocomplete(input, {bounds: lucknowBounds});
    autocomplete.addListener("place_changed", function() {
        // document.getElementsByClassName('search-container')[0].classList.remove('search-container-nav');
        // $('#my-nav-container').css({'display': 'flex'});
        carousel = document.getElementById('search-carousel');
        carousel.style = 'display: block';
        carousel.classList.add('search-carousel-appear');
        $('#c-appartments').click();
        place = document.getElementById('search').value;
        document.getElementById('h-place').setAttribute('data-con', place)
        place = place.split(',')[0]
        document.getElementById('h-place').setAttribute('value', place)
        localStorage.setItem('place', JSON.stringify(place))
        dyn = document.querySelectorAll('.dyn-place');
        dyn.forEach(function ( e){
          e.innerText = place;
        })
        dynCity = document.querySelectorAll('.dyn-city');
        dynCity.forEach(function(e){
          e.innerText = city;
        })

    })
}).catch((error) => {
  // Geocoding failed
  console.log("Geocoding failed:", error);
});

}
function initializeAutocompleteModal() {
const input = document.getElementById('modal-search');
const options = {
  types: ['geocode'],
  componentRestrictions: { country: 'IN' }
};
const autocomplete = new google.maps.places.Autocomplete(input, options);
autocomplete.addListener("place_changed", function() {
  $('#cities-modal').hide();
  city = document.getElementsByClassName('modal-city-search')[0].value;
  console.log(city);
  name = city.split(',')[0]
  document.getElementById('show-city').innerText = name;
  document.getElementById('show-city').setAttribute('data-value', name);
  document.getElementById('h-city').setAttribute('value', name);
  document.getElementById('h-city').setAttribute('data-con', city);
  localStorage.setItem('city', JSON.stringify(name));
  $('#search').focus();
  dyn = document.querySelectorAll('.dyn-city');
  dyn.forEach(function(e){
    e.innerText = name;
  })
})
}
$(document).ready(function () {
  try {
    ls_city = JSON.parse(localStorage.getItem('city'));
    if (ls_city){
      document.getElementById('h-city').value = ls_city;
      console.log(ls_city);
    }
    else {
      localStorage.setItem('city', JSON.stringify('Lucknow'));
    }
    search_modal = document.getElementById('h-city').value;
    console.log(search_modal.length)
    if (search_modal.length < 1){
        document.getElementById('h-city').value = 'Lucknow';
    }
    city = JSON.parse(localStorage.getItem('city'));
    place = JSON.parse(localStorage.getItem('place'));
    dyn = document.querySelectorAll('.dyn-place');
    dyn.forEach(function ( e){
      e.innerText = place;
    })
    dynCity = document.querySelectorAll('.dyn-city');
    dynCity.forEach(function(e){
      e.innerText = city;
    })
    document.getElementsByClassName('lp-dyn-city')[0].value = city;
  }
  catch {
    city = JSON.parse(localStorage.getItem('city'));
    document.getElementsByClassName('lp-dyn-city')[0].value = city;
  }
})
