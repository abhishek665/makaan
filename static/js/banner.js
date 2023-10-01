function checkTypeSelect(e){
    console.log('1', e);
    document.getElementById('check-type-select').value = e;
    
}
function checkPropertyTypeSelect(e){
    console.log(e.id);
    document.getElementById('check-property-type').value = document.getElementById(e.id).getAttribute('data-con');
    if (e.id == 'c-houses'){
        console.log('hou');
        document.getElementById('check-property-type-loader').innerHTML = '<div class="btn-group row" id="houses-loader" role="group" aria-label="Basic checkbox toggle button group">\
        <div class="col-5">\
          <input type="checkbox" class="btn-check" id="btncheck1" autocomplete="off">\
          <label class="btn btn-outline-primary" for="btncheck1">upto 1000sqrft</label>\
        </div>\
        <div class="col-5">\
          <input type="checkbox" class="btn-check" id="btncheck2" autocomplete="off">\
          <label class="btn btn-outline-primary" for="btncheck2"> upto 2000sqrft</label>\
        </div>\
        <div class="col-5">\
          <input type="checkbox" class="btn-check" id="btncheck3" autocomplete="off">\
          <label class="btn btn-outline-primary" for="btncheck3">upto 3000sqrft</label>\
        </div>\
        <div class="col-12">\
        <label class="btn btn-outline-primary" for="btncheck4">\
          <input type="number" class="form-control" placeholder="Enter Manually" id="btncheck4" autocomplete="off">sqrft.\
          </label>\
        </div>\
      </div>';
      $('.builtUpSlider').hide();
    }
    if (e.id == 'c-plots'){
        console.log('plots');
        document.getElementById('check-property-type-loader').innerHTML = '<div class="btn-group row" id="plots-loader" role="group" aria-label="Basic checkbox toggle button group">\
        <div class="col-5">\
          <input type="checkbox" class="btn-check" id="btncheck1" autocomplete="off">\
          <label class="btn btn-outline-primary" for="btncheck1">upto 1000sqrft</label>\
        </div>\
        <div class="col-5">\
          <input type="checkbox" class="btn-check" id="btncheck2" autocomplete="off">\
          <label class="btn btn-outline-primary" for="btncheck2"> upto 2000sqrft</label>\
        </div>\
        <div class="col-5">\
          <input type="checkbox" class="btn-check" id="btncheck3" autocomplete="off">\
          <label class="btn btn-outline-primary" for="btncheck3">upto 3000sqrft</label>\
        </div>\
        <div class="col-12">\
            <label class="btn btn-outline-primary" for="btncheck4">\
          <input type="number" class="form-control" placeholder="Enter Manually" id="btncheck4" autocomplete="off">sqrft.\
          </label>\
        </div>\
      </div>';
      $('.builtUpSlider').hide();
    }
    if (e.id == 'c-appartments'){
        console.log('appar');
        document.getElementById('check-property-type-loader').innerHTML = '<div class="btn-group row" id="appartments-loader" role="group" aria-label="Basic checkbox toggle button group"><div class="col-5">\
          <input type="checkbox" onchange="checkBhkToggler(this);" class="btn-check" id="1bhk" autocomplete="off">\
          <label class="btn btn-outline-primary" for="1bhk">1 BHK</label></div>\
        <div class="col-5">\
          <input type="checkbox" onchange="checkBhkToggler(this);" class="btn-check" id="2bhk" autocomplete="off">\
          <label class="btn btn-outline-primary" for="2bhk"> 2 BHK</label></div>\
        <div class="col-5">\
          <input type="checkbox" onchange="checkBhkToggler(this);" class="btn-check" id="3bhk" autocomplete="off">\
          <label class="btn btn-outline-primary" for="3bhk">3 BHK</label></div>\
        <div class="col-5">\
          <input type="checkbox" onchange="checkBhkToggler(this);" class="btn-check" id="4bhk" autocomplete="off">\
          <label class="btn btn-outline-primary" for="4bhk">3+ BHK</label></div></div>';
          $('.builtUpSlider').show();
    }
}


// budget slider

$(function(){
	$('input[type="range"]').rangeslider({
		polyfill:false,
		onInit:function(){
			$('.header .pull-right').text($('input[type="range"]').val()+'K');
		},
		onSlide:function(position, value){
			//console.log('onSlide');
			//console.log('position: ' + position, 'value: ' + value);
			$('.header .pull-right').text(value+'K');
		},
		onSlideEnd:function(position, value){
			//console.log('onSlideEnd');
			//console.log('position: ' + position, 'value: ' + value);
		}
	});
});

function searchLocalityCityChange(e) {
    // e.preventDefault();
    document.getElementsByClassName('search-container')[0].classList.remove('search-container-nav');
    $('#my-nav-container').css({'display': 'flex'});
    $('#close-search-container-nav').css({'display': 'none'});
    $('body').css({'overflow': 'scroll'})
    $('#show-city-btn').click();
}

// end

function submitListPropertyForm(e){
    budget = document.getElementById('budgetSlider').value;
    built = document.getElementById('builtUpSlider').value;
    document.getElementById('price').value = budget;
    document.getElementById('area').value = built;
    filter = {price: budget, area: built, bhk: JSON.parse(document.getElementById('bhk').value)};
    localStorage.setItem('filter', JSON.stringify(filter));
    $('#search-form').submit();
}
function checkBhkToggler(e){
    bhk_btn_value = e.value;
    if (bhk_btn_value == 'on'){
        bhk_form_val = document.getElementById('bhk');
        val = bhk_form_val.value;
        current = e.id;
        if (!val.includes(current)){
            console.log('entering value')
            val.push(current)
            console.log(val)
            bhk_form_val.value = val;
        }
        e.value = 'off'
    }
    else{
        bhk_form_val = document.getElementById('bhk');
        val = bhk_form_val.value;
        current = e.id;
        const newVal = val.filter(item => item !== current);
        console.log(newVal, current, 'iiiiiiiiii');
        bhk_form_val.value = newVal;
        e.value = 'on';  
    }
}