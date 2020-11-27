# Pi-Approximation-using-Leibniz-formula
In this program, I use Leibniz formula to approximate the value of pi ( π ), Its one of the simplest way u can approximate pi

# About Leibniz formula
the Leibniz formula for π, named after Gottfried Leibniz, states that<br><br>
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/0987be72b10e739db97b8c457a9baf875bf47710"><br><br>
an alternating series. It is also called the Madhava–Leibniz series as it is a special case of a more general series expansion for the inverse tangent function, first discovered by the Indian mathematician Madhava of Sangamagrama in the 14th century, the specific case first published by Leibniz around 1676. The series for the inverse tangent function, which is also known as Gregory's series, can be given by:
<br><br>
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/fc798b313be2383b0ab34e70e81a318756745051"><br><br>
The Leibniz formula for 
π
/
4
 can be obtained by putting x = 1 into this series.
 
 # My Instagram post on the same topic
 <a href="https://www.instagram.com/p/CHpHNS_DyQR/?utm_source=ig_web_copy_link"><img src="https://instagram.fdel3-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/125261883_163232248841608_8009125204969336481_n.jpg?_nc_ht=instagram.fdel3-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=tDCx78jgIFUAX_2-KZy&tp=1&oh=4485400271eddf0e5df23f12236437bf&oe=5FEAEB8E" width="350em"><br>Click on the photo!</a>
 
 <br>
 <p align="center">
 <a href="https://www.instagram.com/mathsyoudontknow/">Follow my Maths Page on Instagram<br><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png" width="100em" ></a> 
 </p>
 
 # Proof
 <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/05ff8f37d93c9b5dafe66b5bdcf74a82d92d63fb">
 <br>
 Considering only the integral in the last line, we have:
 <br>
 <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/60d30bdd33b34290568c0e13da19503de36cf1e9">
 <br>
 Therefore, by the squeeze theorem, as n → ∞ we are left with the Leibniz series:
 <br>
 <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/cfa16105f38678c4b8151cd1ac1cd1a0a8d219c6">
 
 <br>
 <h2>Its as simple as that😊</h2>
 
 # Dependencies
 <ul>
  <li>Matplotlib <br>
    <code> pip install matplotlib </code>
  </li>
  <br>
  <li>Numpy<br>
    <code> pip install numpy</code>
  </li>
  </ul>
  
  # Output
  Output is a scatterplot between, approximated value of pi and number of terms in the series(starting from 0)<br>
  In this example, we have just 1000 terms, you can have as many as you want.<br>
  <img src="https://github.com/beetrandahiya/Pi-Approximation-using-Leibniz-formula/blob/main/piaproxxoutput1.PNG">
  <br>
  If you zoom you can see the points on graph more clearly
  <br>
  
  <img src="https://github.com/beetrandahiya/Pi-Approximation-using-Leibniz-formula/blob/main/piaproxxoutput.PNG">
  <br>
  Zoomed in at the end of series 
  
 <br> Error is also printed alongside every value of pi in terminal
          
  <img src="https://github.com/beetrandahiya/Pi-Approximation-using-Leibniz-formula/blob/main/piaproxxoutput2.PNG">
