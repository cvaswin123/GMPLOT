
# import gmplot package 
import gmplot 
#List of latitude and longitude of the required locations  
latitude_list = [  8.48712234,8.48557308 , 8.48440582,8.48345079 , 8.48190152] 
longitude_list = [ 76.98077202,76.98085785, 76.98117971,76.98115826,76.98193073 ] 
  
gmap3 = gmplot.GoogleMapPlotter(8.48440582 ,76.98117971 , 17) 
  
# Plot method Draw a line in 
# between given coordinates 
gmap3.plot(latitude_list, longitude_list,  
           'cornflowerblue', edge_width = 2.5)
# Mark each coordinates
gmap3.marker(8.48712234 ,76.98077202,color='red') 
gmap3.marker(8.48557308 ,76.98085785 ,color='red') 
gmap3.marker( 8.48440582 ,76.98117971,color='red') 
gmap3.marker(8.48345079 ,76.98115826,color='red') 
gmap3.marker( 8.48190152 ,76.98193073,color='red') 
# Type your API key
gmap3.apikey = "AIzaSyCXZOLKY1Hnw3DTTug4IbYgExumDVC_J_s"
gmap3.draw( "C:\\Users\\user\\Desktop\\map13.html" ) 
