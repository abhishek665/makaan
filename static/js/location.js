

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        console.log("Latitude: " + latitude);
        console.log("Longitude: " + longitude);
        
        // You can perform further actions with the obtained coordinates here
        const geocoder = new google.maps.Geocoder();

        const latlng = {
        lat: latitude,
        lng: longitude
        };

    geocoder.geocode({ location: latlng }, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
        if (results[0]) {
        const address = results[0].formatted_address;
        console.log("Address: " + address);
        
        // You can perform further actions with the obtained address here
        } else {
        console.log("No results found");
        }
    } else {
        console.log("Geocoder failed due to: " + status);
    }
    });

      },
      function(error) {
        console.log("Error retrieving location: " + error.message);
      }
    );
  } else {
    console.log("Geolocation is not supported by this browser.");
}
