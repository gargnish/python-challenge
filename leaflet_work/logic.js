///////////////////////////////////////////////////////////////// 
//data setup

var queryUrl1 = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

  var f1 = function(row){
      return row;
  };
  
  
						
queryUrl2 = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_plates.json";
						
  var f2 = function(row){
      return row;
  };
  
	
 
var promise1 = d3.json(queryUrl1, f1);
var promise2 = d3.json(queryUrl2, f2);


Promise.all([promise1, promise2]).then(function(v_result_list) {
  console.log(v_result_list);
  fx_root (v_result_list);
});



// expected output: Array [result1, result2]


 ///////////////////////////////////////////////////////////////


function fx_root (v_result_list) {
			
			//////  setting up layering container

		v_access_token1 = "pk.eyJ1IjoibmlzaGdhcmciLCJhIjoiY2pneWV4MjFrMDRrdjJ3cWxnaWZ3cTNsdiJ9.J4VAPeTQnbh5jryTIfJAPQ"

		v_tile_layer1 = "https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?access_token=" + v_access_token1

		v_tile_layer2 = "https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?access_token=" + v_access_token1

		v_tile_layer3 = "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/256/{z}/{x}/{y}?access_token=" + v_access_token1

				
				
		v_tile_layer1_casted = L.tileLayer(v_tile_layer1)
		v_tile_layer2_casted = L.tileLayer(v_tile_layer2)
		v_tile_layer3_casted = L.tileLayer(v_tile_layer3)

		Layer_container1 = {
					   "Satellite": v_tile_layer3_casted,
		               "Grayscale": v_tile_layer2_casted,
		  		      "Outdoors": v_tile_layer1_casted
		};

//////  runtime start
		fx_overlay_data1(v_result_list[0]);
		fx_overlay_data2(v_result_list[0]);
		fx_overlay_data3 (v_result_list[0]);
		fx_overlay_data4 (v_result_list[0]);
		fx_overlay_data5 (v_result_list[1]);
		fx_map_attach(); 
//////  runtime end 


////////////fx_overlay_data1 start /////
		function fx_overlay_data1 (my_geo_data_raw1) {list_overlay_1_casted = L.geoJSON(my_geo_data_raw1 ) };
////////////fx_overlay_data1 end /////

		////////////fx_overlay_data2 start /////
				function fx_overlay_data2 (my_geo_data_raw2) {

					list_overlay_2_casted = L.markerClusterGroup();


					  for (var i = 0; i < my_geo_data_raw2.features.length; i++) {
						var v_location = my_geo_data_raw2.features[i].geometry;
						var v_descriptor = "<h3>" + my_geo_data_raw2.features[i].properties.title +
							  "</h3><hr><p>" + new Date(my_geo_data_raw2.features[i].properties.time) + "</p>"

						if (v_location) {
						 
						 // Add a new marker to the cluster group and bind a pop-up
						  list_overlay_2_casted.addLayer(L.marker([v_location.coordinates[1], v_location.coordinates[0]])
							.bindPopup(v_descriptor));
										 }
						 
						 
						}

					
				};
		////////////fx_overlay_data2 end /////

////////////fx_overlay_data3 start /////	
function fx_overlay_data3 (my_geo_data_raw3) {
					list_overlay_3_casted = L.geoJSON(my_geo_data_raw3 , { pointToLayer: fx_pointToLayer, style : fx_style , onEachFeature: fx_onEachFeature  });
													
						function fx_pointToLayer( v_feature_row, latlng) {

						var v_geojsonMarkerOptions = {
							radius: fx_chooseColor(v_feature_row.properties.mag).radius,
							//radius: 10,
							fillColor: fx_chooseColor(v_feature_row.properties.mag).color,
							color: fx_chooseColor(v_feature_row.properties.mag).color,
							weight: 1,
							opacity: 1,
							fillOpacity: 0.8,
							title: v_feature_row.properties.title
						};

						return L.circleMarker(latlng, v_geojsonMarkerOptions)
								.bindPopup("<h3>" + v_feature_row.properties.title +
      "</h3><hr><p>" + new Date(v_feature_row.properties.time) + "</p>");

						};	

						/////////function definitions 
						function fx_chooseColor(mag) {
						
							v_mag = + mag	
						if (v_mag < 1) {
							v_color = '#00ff40';
							v_color_label = '0-1';
							v_radius = 3;
						} else if (v_mag < 2) {
							v_color = '#bfff00';
							v_color_label = '1-2';
							v_radius = 6;
						} else if (v_mag < 3) {
							v_color = '#ffff00';
							v_color_label = '2-3';
							v_radius = 8;
						} else if (v_mag < 4) {
							v_color = '#ffbf00';
							v_color_label = '3-4';
							v_radius = 10;
						} else if (v_mag < 5) {
							v_color = '#ff8000';
							v_color_label = '4-5'; 
							v_radius = 12;
						} else {
							v_color = '#ff0000';
							v_color_label = '5+';
							v_radius = 15;
						}

						return {
							'color' : v_color,
							'color_label' : v_color_label,
							'radius'  : v_radius
						}

						};



						function fx_style (v_feature_row) {
							return {
								color: fx_chooseColor(v_feature_row.properties.mag).color,
								// Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
								fillColor: fx_chooseColor(v_feature_row.properties.mag).color,
								fillOpacity: 0.5,
								weight: 1.5
							  };
						}

						function fx_onEachFeature(v_feature_row, layer_chain) {
								  // Set mouse events to change map styling
							  layer_chain.on({
								// When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
								mouseover: function(x_event) {
								  v_layer1 = x_event.target;
								  v_layer1.setStyle({
									fillOpacity: 0.9
								  });
								},
								// When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
								mouseout: function(x_event) {
								  v_layer2 = x_event.target;
								  v_layer2.setStyle({
									fillOpacity: 0.5
								  });
								}
								
							  });
							  // Giving each feature a pop-up with information pertinent to it
							
							//layer_chain.bindPopup("<h1>" + v_feature_row.properties.neighborhood + "</h1> <hr> <h2>" + v_feature_row.properties.borough + "</h2>");
						  };			
									
									
									

									
									
									
					// setting up legend control box 

					v_control_legend_box = L.control({ position: "bottomright" });


					  v_control_legend_box.onAdd = fx_legend;
					  
					  
					  
					  function fx_legend () {
					    v_limits = ['0-1','1-2','2-3','3-4','4-5','5+'];
					    v_colors = ['#00ff40','#bfff00','#ffff00','#ffbf00','#ff8000','#ff0000'];

						
					   v_div = L.DomUtil.create("div", "info legend");
					  
                       v_div.innerHTML = "<h4 style='margin:4px'>Magnitude</h4>"
   
					   for (var i = 0; i < v_limits.length; i++) {
								v_div.innerHTML +=
									'<i style=" width: 25px;height: 22px;display: inline-block ; background:' + v_colors[i] + '"></i> ' +
									v_limits[i]  + '<br>' 
											  }

						    return v_div;
					  };
					  
					  
					  
					
					        
};	    
////////////fx_overlay_data3 end /////					
			


////////////fx_overlay_data4 start /////					
						function fx_overlay_data4 (my_geo_data_raw4) {
							//list_overlay_4_casted = L.geoJSON(my_geo_data_raw4);
							
							
							// setting up the data 
							  var v_heatArray = [];

							  for (var i = 0; i < my_geo_data_raw4.features.length; i++) {

								var v_location = my_geo_data_raw4.features[i].geometry.coordinates;

								if (v_location) {
								  v_heatArray.push([v_location[1], v_location[0] ])
								}
							  }

							  list_overlay_4_casted = L.heatLayer(v_heatArray, {
								radius: 10,
								minOpacity: 0.8,
								blur: 10 ,
								gradient : {0.4: 'blue', 0.65: 'lime', 1: 'red'}
							  })
							  
							  
							  
						};						  
////////////fx_overlay_data4 end /////						
						
							
							
////////////fx_overlay_data5 start /////					
							function fx_overlay_data5 (my_geo_data_raw5) {
								list_overlay_5_casted = L.geoJSON(my_geo_data_raw5);
							};			
	////////////fx_overlay_data5 start /////	

/////////////////////////////// map attachment started 
				function fx_map_attach () {
					

						overlay_container2 = {
						  "Standard" : list_overlay_1_casted,
						  "Clustering" : list_overlay_2_casted,
						  "Circles" : list_overlay_3_casted,
						  "Heatmap" : list_overlay_4_casted,
						  "Tectonic plates" : list_overlay_5_casted
						  
						};
	
						v_my_default_showing = [v_tile_layer1_casted , list_overlay_3_casted ]


						v_map_option_dict = {
						  center: [ 37.7749, -122.4194],
						  zoom: 2 ,
						  minZoom: 2,
						  layers : v_my_default_showing,
						  maxBounds: L.latLngBounds([90, -180], [-90, 180]),
							maxBoundsViscosity: 1,
						}

						var myMap = L.map("map", v_map_option_dict );

						//////  setting up control box and adding to map  
						v_control_box = L.control.layers(Layer_container1,overlay_container2, {
						  collapsed: false
						});
						v_tile_layer1_casted.addTo(myMap)
						
						v_control_box.addTo(myMap);
						v_control_legend_box.addTo(myMap);
						
						
						//  var sliderControl = L.control.sliderControl({position: "topright", layer: list_overlay_3_casted});
					  
									
					    // Playback options
					     playbackOptions = {
					        playControl: true,
					        dateControl: true,
					        sliderControl: true     
					    };
						
						
						//sliderControl.addTo(myMap);
							// Initialize playback
//var playback = new L.Playback(list_overlay_3_casted,  v_result_list[0].features, null, playbackOptions);   
//list_overlay_3_casted.addTo(myMap)

				
				// fx_map_attach ending below 
				};
								

// fx_root ending below 
};


