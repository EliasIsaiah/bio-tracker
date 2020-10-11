## Bio-Tracker 🌎 🌱 📈

Tackling the `Sustain` Challenge

### Objective
Using carnivorous Sundew plants and Sphagnum to improve air quality on the ISS and future Space exploration missions 

Sphagnum:

![Sphagnum](https://upload.wikimedia.org/wikipedia/commons/2/22/Sphagnum.flexuosum.jpg)
### What are, and why, sundews and spagnham?
Sundews are small, palm-size, carnivorous plants that trap and digest prey via mucilaginous glands that cover their leaf surfaces. Sphagnum is a type of moss, otherwise known as peat moss, that absorbs many times its weight in water and can develop anaerobic soil conditions. Both are crucial parts of wetland ecosystems, but may pose as an interesting tool in combating air quality issues when used together. Poor air quality is a threat to sustaining life on earth and expanding our existence off planet and has been shown to trigger asthma and diabetes. 

One aspect that decreases air quality is dust, which is largely composed of dead skin flakes.

Though most plants undergo photosynthesis and have a critical part in Earth’s respiration cycle, carnivorous plants add a unique aspect to this equation due to their ability to extract nutrients from prey, such as insects. With external nutrient availability, they are more resistant to pests and able to grow in less nutrient dense environments. Carnivorous plants, such as sundews can also extract nutrients from flakes of skin, or dust particles. 

Sundew:

![Sundew](https://images-images-images.s3.amazonaws.com/Carnivorous_sundew_plant-Drosera_rotundifolia_%25287.png)

### The Application

#### As an individual conducting Sundew and Sphagnum experiments, I want to be able to track the health of the specimens and the environmental conditions affecting it, and I want to store the data for use in statistical analyses.

Technologies:
* Database: Kintone
Using Kintone a database can be quickly spun up with all of the different fields that are required for tracking the specimens’ status.
The database can be queried by the client via Kintone’s RESTful API without much work done on the developer’s end, which is convenient.

* Back End: Python (Django)
Chosen for stability as Python is more stable than the other likely alternative Node.js
Python is well supported in the scientific community, which will be a boon for integrating further features as the project grows

* Front End: Vue.js
Vue is chosen for its ease of use and rapid development.

UI Mockup:
![UI PoC](https://images-images-images.s3.amazonaws.com/rough_ui.gif)

### Link to Project Presentation: 
[Presentation](https://docs.google.com/presentation/d/1LubCbh_YUnwEIIW3Us12WvGsC8I_FJMp206XBMlX57k/edit?usp=sharing)

### References
1. B. Duncan, "Particulate Matter," Air Quality Observations from NASA, 10 July 2020. [Online]. Available: https://airquality.gsfc.nasa.gov/particulate-matter. [Accessed 03 Oct 2020].
2. NASA, "Closing the Loop: Recycling Water and Air in Space," p. 7.
3. M. P. H. L. I. K. L. Wolfram Adlassnig, "The roots of carnivorous plants," Springer - Plant and Soil, vol. 274, p. 14, 2005.
4. C. White, "Effect of Increased Atmospheric Nitrogen Deposition and Elevated CO2 on Traits Responsible for Carnivory in the Sundews Drosera rotundifolia and Drosera intermedia," p. 31, 2015.
5. "Plants release up to 30 per cent more CO2 than previously thought, study says," News, 21 Nov 2017. [Online]. Available: https://www.abc.net.au/news/2017-11-18/plant-respiration-co2-findings-anu-canberra/9163858#:~:text=During%20daylight%20hours%2C%20plants%20take,absorb%20more%20than%20they%20emit. [Accessed 02 October 2020].
6. A. S. M. M. E. B. E. G. G. W. E. L. Aleksandra Krolicka, "Antibacterial and antioxidant activity of the secondary metabolites from in vitro cultures of the Alice sundew (Drosera aliciae)," Biotechnology and Applied Biochemistry, vol. 53, p. 3, 2009.
7. T. Pultarova, "This Space Station Air Recycler Could Help Astronauts Breathe Easier on Mars," SPACE.COM, 7 Nov 2018. [Online]. Available: https://www.space.com/42362-space-station-air-recycler-for-mars-astronauts.html. [Accessed 03 October 2020].
8. H. I. H. Y. A. M. Y. S. Naoko Yoshida, "Aquatic plant surface as a niche for methanotrophs," Frontiers in Microbiology, vol. 5, p. 30, 2014.
9. P. L. Barry, "Breathing Easy on the Space Station," NASA SCIENCE SHARE THE SCIENCE, 12 Nov 2000. [Online]. Available: https://science.nasa.gov/science-news/science-at-nasa/2000/ast13nov_1/. [Accessed 03 Oct 2020].
10. "Cities of World Ranked by Exposure to Particulates," Pollution Free Cities, 14 Oct 2011. [Online]. Available: https://pollutionfree.wordpress.com/2011/10/14/cities-of-world-ranked-by-exposure-to-particulates/. [Accessed 03 Oct 2020].
