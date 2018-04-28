// Setting a variable for flexibility in future functionality of variable source
dataSet_orig = dataSet


//-----------------------------------------------------------------------------------------------------------------------------------
//------------------initial population of dropdowns ------------------------------
fx_populate_dropdown ();

//-----------------------------------------------------------------------------------------------------------------------------------
//------------------population of dropdowns on change ------------------------------
$e_country_select= document.getElementById('id_country');
$e_country_select.addEventListener("change", fx_populate_dropdown , false);


$e_state_select= document.getElementById('id_state');
$e_state_select.addEventListener("change", fx_populate_dropdown, false);


$e_shape_select= document.getElementById('id_shape');
$e_shape_select.addEventListener("change", fx_populate_dropdown, false);


//-----------------------------------------------------------------------------------------------------------------------------------
// ------------search hide and display TRIGGER
$e_searchnav_select= document.getElementById('id_searchnav_action');
$e_searchnav_select.addEventListener("click", fx_searchnav);
$e_searchnav= document.getElementById('id_searchnav');

function fx_searchnav(event) {
  if  ($e_searchnav_select.textContent == 'Hide Search bar')  {
    event.preventDefault();
    $e_searchnav.classList.add("d-none");
    $e_searchnav_select.textContent = 'Advance Search';
    console.log('I am here inside');
  }
  else if ($e_searchnav_select.textContent == 'Advance Search') {
    event.preventDefault();
    $e_searchnav.classList.remove("d-none");
    $e_searchnav_select.textContent = 'Hide Search bar';
    //    $e_searchnav.className = $e_searchnav.className.replace(/\bd-none\b/g, "");
  };
};

//-----------------------------------------------------------------------------------------------------------------------------------
// ------------background hide and display TRIGGER

function fx_backgroud(v_action) {
  $e_id_bg_image= document.getElementById('id_bg_image');
  $e_id_table_div= document.getElementById('id_table_div');
  if  (v_action == 'show')  {
    $e_id_bg_image.classList.remove("d-none");
    $e_id_table_div.classList.add("d-none");
  }
  else if (v_action == 'hide') {
    $e_id_bg_image.classList.add("d-none");
    $e_id_table_div.classList.remove("d-none");
  };
};

//-----------------------------------------------------------------------------------------------------------------------------------
//-------------------- fx_dropdown function to display dropdowns
function fx_dropdown(v_list_of_dict1,v_dom_id  , v_default_value) {
  console.log(v_default_value);
  document.getElementById(v_dom_id).length = 0 ;
  var x = document.createElement("option");
  x.setAttribute("value", v_default_value);
  x.setAttribute("selected", true);
  var t = document.createTextNode(v_default_value);
  x.appendChild(t);
  document.getElementById(v_dom_id).appendChild(x);

  var f1 = function(s) { 
    var x = document.createElement("option");
    x.setAttribute("value", s['dropdown_value']);
    var t = document.createTextNode(s['dropdown_display']);
    x.appendChild(t);
    document.getElementById(v_dom_id).appendChild(x);
  };

  v_list_of_dict1.forEach(f1);

};

//-----------------------------------------------------------------------------------------------------------------------------------
//-------------------- fx_populate_dropdown ---dynamic data calculation for dropdowns

function fx_populate_dropdown ()  {
  v_country_value = document.getElementById("id_country").value
  v_state_value = document.getElementById("id_state").value
  v_city_value = document.getElementById("id_city").value
  v_from_date_value = document.getElementById("id_from_date").value
  v_to_date_value = document.getElementById("id_to_date").value
  v_shape_value = document.getElementById("id_shape").value

  v_filtered_dataset_dict = dataSet_orig;

  if  ( (v_country_value !=  'select country') && (v_country_value !=  '') ) {
    v_filtered_dataset_dict = v_filtered_dataset_dict.filter (function (i) { return i['country'] ==v_country_value });
    console.log('i am here');

  };	


  if ((v_state_value !=  'select state') && (v_state_value !=  '')){
    v_filtered_dataset_dict = v_filtered_dataset_dict.filter (function (i) { return i['state'] ==v_state_value });
    console.log('x'+v_state_value+'y');
    console.log('i am here1');
  };	


  if ((v_shape_value !=  'select shape') && (v_shape_value !=  '') ) {
    v_filtered_dataset_dict = v_filtered_dataset_dict.filter (function (i) { return i['shape'] ==v_shape_value });
    console.log('i am here2');
  };	

  //------------------ country code ------------------------------

  console.log(v_filtered_dataset_dict);

  v_country_list = v_filtered_dataset_dict.map (x => x['country']);
  v_country_list = v_country_list.filter(function(n){ return n != undefined }); 
  v_country_uk_list = Array.from(new Set(v_country_list)).sort();
  v_list_of_dict = v_country_uk_list.map (x => ({'dropdown_display' : x , 'dropdown_value' : x} ) );
  fx_dropdown (v_list_of_dict , 'id_country' , v_country_value);

  //------------------ state code ------------------------------

  v_state_list = v_filtered_dataset_dict.map (x => x['state']);
  v_state_list = v_state_list.filter(function(n){ return n != undefined }); 
  v_state_uk_list = Array.from(new Set(v_state_list)).sort();
  v_list_of_dict = v_state_uk_list.map (x => ({'dropdown_display' : x , 'dropdown_value' : x} ) );
  fx_dropdown (v_list_of_dict , 'id_state' , v_state_value);

  //------------------ shape code ------------------------------

  v_shape_list = v_filtered_dataset_dict.map (x => x['shape']);
  v_shape_list = v_shape_list.filter(function(n){ return n != undefined }); 
  v_shape_uk_list = Array.from(new Set(v_shape_list)).sort();
  v_list_of_dict = v_shape_uk_list.map (x => ({'dropdown_display' : x , 'dropdown_value' : x} ) );
  fx_dropdown (v_list_of_dict , 'id_shape' , v_shape_value);

};

//-----------------------------------------------------------------------------------------------------------------------------------
//-------------------- fx_reset_dropdown ---reseting dropdowns to original value in the end

function fx_reset_dropdown () {

  //------------------ country code ------------------------------
  v_filtered_dataset_dict = dataSet_orig;

  v_country_list = v_filtered_dataset_dict.map (x => x['country']);
  v_country_list = v_country_list.filter(function(n){ return n != undefined }); 
  v_country_uk_list = Array.from(new Set(v_country_list)).sort();
  v_list_of_dict = v_country_uk_list.map (x => ({'dropdown_display' : x , 'dropdown_value' : x} ) );
  fx_dropdown (v_list_of_dict , 'id_country' , 'select country');

  //------------------ state code ------------------------------

  v_state_list = v_filtered_dataset_dict.map (x => x['state']);
  v_state_list = v_state_list.filter(function(n){ return n != undefined }); 
  v_state_uk_list = Array.from(new Set(v_state_list)).sort();
  v_list_of_dict = v_state_uk_list.map (x => ({'dropdown_display' : x , 'dropdown_value' : x} ) );
  fx_dropdown (v_list_of_dict , 'id_state' , 'select state');

  //------------------ shape code ------------------------------

  v_shape_list = v_filtered_dataset_dict.map (x => x['shape']);
  v_shape_list = v_shape_list.filter(function(n){ return n != undefined }); 
  v_shape_uk_list = Array.from(new Set(v_shape_list)).sort();
  v_list_of_dict = v_shape_uk_list.map (x => ({'dropdown_display' : x , 'dropdown_value' : x} ) );
  fx_dropdown (v_list_of_dict , 'id_shape' , 'select shape');

  //------------------ reset city ------------------------------
  $e_city_id = document.getElementById("id_city")
  
  $e_city_id.placeholder = 'city' ;
  $e_city_id.value = 'city' ;

  //------------------ reset from_date ------------------------------
  $e_from_date_id = document.getElementById("id_from_date")
  $e_from_date_id.placeholder = 'From Date' ;
  $e_from_date_id.value = '' ;
  
  //------------------ reset to_date ------------------------------
  
  $e_to_date_id = document.getElementById("id_to_date")
  $e_to_date_id.placeholder = 'To Date' ;
  $e_to_date_id.value = '' ;
  
};


//-----------------------------------------------------------------------------------------------------------------------------------
//-----------------search submit action----------------------

$e_search= document.getElementById('id_search');
$e_search.addEventListener("click", fx_search);

function fx_search(event) {
  event.preventDefault();
  
  var $e_selection_text= document.getElementById("id_selection_text");
  $e_selection_text.innerHTML = 'Total records found = 0';
  fx_backgroud('show');
  
  v_country_value = document.getElementById("id_country").value
  v_state_value = document.getElementById("id_state").value
  v_city_value = document.getElementById("id_city").value
  v_from_date_value = document.getElementById("id_from_date").value
  v_to_date_value = document.getElementById("id_to_date").value
  v_shape_value = document.getElementById("id_shape").value

  v_filtered_list_of_dict = dataSet_orig;

  if (v_country_value !=  'select country') {
    v_filtered_list_of_dict = v_filtered_list_of_dict.filter (function (i) { return i['country'] ==v_country_value });
  };

  if (v_state_value !=  'select state') {
    v_filtered_list_of_dict = v_filtered_list_of_dict.filter (function (i) { return i['state'] ==v_state_value });
  };	

  if ( (v_city_value !=  '') && (v_city_value !=  'city')) {
    v_filtered_list_of_dict = v_filtered_list_of_dict.filter (function (i) { return i['city'] ==v_city_value });
  };		

  if (v_shape_value != 'select shape') {
    v_filtered_list_of_dict = v_filtered_list_of_dict.filter (function (i) { return i['shape'] ==v_shape_value });
  };	

  if (v_from_date_value !=  '') {
    v_filtered_list_of_dict = v_filtered_list_of_dict.filter (function (i) {
      v_dataset_value = moment(i['datetime'], 'MM/DD/YYYY').format('YYYY-MM-DD');
      return  v_dataset_value  >= v_from_date_value });
  };		

  if (v_to_date_value !=  '') {
    v_filtered_list_of_dict = v_filtered_list_of_dict.filter (function (i) {
      v_dataset_value = moment(i['datetime'], 'MM/DD/YYYY').format('YYYY-MM-DD');
      return  v_dataset_value  <= v_to_date_value });
  };		

  v_total_search_results = v_filtered_list_of_dict.length;
  v_page_id = 1;
  fx_table (v_filtered_list_of_dict , 'id_table' , v_page_id);

  if (v_total_search_results > 0) {
  fx_backgroud('hide');
  }
  else {
    fx_backgroud('show');
  }
  ;
};

//-----------------------------------------------------------------------------------------------------------------------------------
//-----------------pagination next action----------------------

$e_page_next= document.getElementById('id_page_next');
$e_page_next.addEventListener("click", fx_next_page);

$e_page_previous_item= document.getElementById('id_page_previous_item');
$e_page_previous= document.getElementById('id_page_previous');

function fx_next_page(event) {
  v_page_id = v_page_id + 1;

  fx_table (v_filtered_list_of_dict , 'id_table' , v_page_id);

  if (v_page_id > 1) {
    $e_page_previous.classList.remove("disabled");
    $e_page_previous_item.classList.remove("disabled");
  }
  else {
    $e_page_previous.classList.add("disabled");
    $e_page_previous_item.classList.add("disabled");
  };
  
};

//-----------------------------------------------------------------------------------------------------------------------------------
//-----------------pagination previous action----------------------


$e_page_previous_item= document.getElementById('id_page_previous_item');
$e_page_previous= document.getElementById('id_page_previous');
$e_page_previous.addEventListener("click", fx_previous_page);

function fx_previous_page(event) {
  
  if (v_page_id > 1 ) {
    v_page_id = v_page_id -1;
    fx_table (v_filtered_list_of_dict , 'id_table' , v_page_id);
  };

  if (v_page_id > 1) {
    $e_page_previous.classList.remove("disabled");
    $e_page_previous_item.classList.remove("disabled");
  }
  else {
    $e_page_previous.classList.add("disabled");
    $e_page_previous_item.classList.add("disabled");
  };
  
};

//-----------------------------------------------------------------------------------------------------------------------------------
//-----------------last month click action ----------------------

$e_last_month= document.getElementById('id_last_month');
$e_last_month.addEventListener("click", fx_last_month);

function fx_last_month(event) {

  var $e_selection_text= document.getElementById("id_selection_text");
  $e_selection_text.innerHTML = 'Total records found = 0';
  fx_backgroud('show');
  
  v_last_month_date_value = moment().subtract(30, 'days').format('YYYY-MM-DD');
  v_filtered_list_of_dict = dataSet_orig;
  //-----
  v_filtered_list_of_dict = v_filtered_list_of_dict.filter (function (i) {
    v_dataset_value = moment(i['datetime'], 'MM/DD/YYYY').format('YYYY-MM-DD');
    return  v_dataset_value  >= v_last_month_date_value });
  //-----
  v_total_search_results = v_filtered_list_of_dict.length;
  v_page_id = 1;
  
  if (v_total_search_results > 0) {
    fx_backgroud('hide');
  }
  else {
    fx_backgroud('show');
  }
  ;

  fx_table (v_filtered_list_of_dict , 'id_table' , v_page_id);
};

//-----------------------------------------------------------------------------------------------------------------------------------
//-----------------last_7_days click action ----------------------

$e_last_7_days= document.getElementById('id_last_7_days');
$e_last_7_days.addEventListener("click", fx_last_7_days);

function fx_last_7_days(event) {

  var $e_selection_text= document.getElementById("id_selection_text");
  $e_selection_text.innerHTML = 'Total records found = 0';
  fx_backgroud('show');
   
  v_last_7_days_date_value = moment().subtract(7, 'days').format('YYYY-MM-DD')
  v_filtered_list_of_dict = dataSet_orig;
   //-----
  v_filtered_list_of_dict = v_filtered_list_of_dict.filter (function (i) {
    v_dataset_value = moment(i['datetime'], 'MM/DD/YYYY').format('YYYY-MM-DD');
    return  v_dataset_value  >= v_last_7_days_date_value });
    //-----
  v_total_search_results = v_filtered_list_of_dict.length;
  v_page_id = 1;

  if (v_total_search_results > 0) {
    fx_backgroud('hide');
  }
  else {
    fx_backgroud('show');
  }
  ;
 
  fx_table (v_filtered_list_of_dict , 'id_table' , v_page_id);
};

//-----------------------------------------------------------------------------------------------------------------------------------
//------------search results population 

function fx_table( v_filtered_list_of_dict , v_dom_id ,v_page_id ){
  //---function assumes that first dict has all the columns
  v_page_size = 10 ;
  x = (v_page_id -1)  * v_page_size;
  y = v_page_id * v_page_size;
  v_list_of_dict_paginated = v_filtered_list_of_dict.slice ( x,y)

  var $e_table= document.getElementById(v_dom_id);
  var $e_header =  $e_table.querySelector("thead");
  var $e_tbody =  $e_table.querySelector("tbody");

  // Start the table body  and header with a blank HTML
  $e_tbody.innerHTML = "";
  $e_header.innerHTML = "";

  var v_result_data_set = v_list_of_dict_paginated;
  var v_header_col_list = Object.keys(v_list_of_dict_paginated[0]);

  //---header population 
  var row = $e_header.insertRow(0);
    for (var k = 0; k < v_header_col_list.length; k++) {
      var  th = document.createElement('th');
		th.innerHTML = v_header_col_list[k];
		row.appendChild(th);
  };
  //----
  
  // The outer loop fills the rows
  // The inner loop fills the cells for each row
  for (var i = 0; i < v_result_data_set.length; i++) {
    // Insert a row into the table at position i
    var $row = $e_tbody.insertRow(i);
    d1 =  v_result_data_set[i];

    for (var j = 0; j < v_header_col_list.length; j++) {
      var $cell = $row.insertCell(j);
      $cell.innerText = d1[v_header_col_list[j]]; 
    }

  }

  fx_reset_dropdown();

  v_selection_text = ''

  if (v_country_value.replace('select country','') != '')  { v_selection_text = v_selection_text + 'country = ' + v_country_value.replace('select country','') + '  ;  ' ; }
  if (v_state_value.replace('select state','') != '')  {  v_selection_text = v_selection_text + 'state = ' + v_state_value.replace('select state','')+ '  ; '; }
  if (v_shape_value.replace('select shape','') != '')  { v_selection_text = v_selection_text + 'shape = ' + v_shape_value.replace('select shape','')+ '  ; '; }
  if (v_from_date_value != '')  { v_selection_text = v_selection_text + 'From date = ' + v_from_date_value+ '  ; '; }
  if (v_to_date_value != '')  { v_selection_text = v_selection_text + 'To date = ' + v_to_date_value+ '  ; '; }
  if ( (v_city_value != '') && (v_city_value !=  'city') ) {  v_selection_text = v_selection_text + 'city = ' + v_city_value+ '  ; '; }

  v_selection_text = v_selection_text + '<br> </br>' + 'Total records found = ' + v_total_search_results+ ' ; '
  v_selection_text = v_selection_text  + 'Number of records per page = ' + v_page_size+ ' ; '
  v_selection_text = v_selection_text +  '   Showing page ' + v_page_id+ ' of  ' + Math.ceil(v_total_search_results/v_page_size) 

  var $e_selection_text= document.getElementById("id_selection_text");
  $e_selection_text.innerHTML = v_selection_text;

  //-----pagination nav

  $e_pagenav= document.getElementById('id_pagenav');
  if  (v_total_search_results> v_page_size)  {
    $e_pagenav.classList.remove("d-none");
  };
  if  (v_total_search_results < v_page_size) {
    $e_pagenav.classList.add("d-none");
  };
  //-----


};

//-----------------------------------------------------------------------------------------------------------------------------------
//-----------------------------------------------------------------------------------------------------------------------------------


