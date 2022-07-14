# Distance Functions and Prodecural Lakes

## Heightmap

Height maps are generated by multiplying several layers of Perlin noise at differing amplitudes and frequencies. See [octave perling noise](https://github.com/devpin95/MeshGenerator#octave-noise) for more infomation on generating heightmaps in this way.

## Distance functions
Distance functions are functions that map a value from 0 to 1 based on the distance a pixel is from the center of the image.

| Name             | Function                                                                         | Output                                              |
|------------------|-----------------------------------------------------------------------|-----------------------------------------------------|
|Distance Squared| x<sup>2</sup> + y<sup>2</sup> | <img src="http://dpiner.com/images/DistanceSquared.jpg"> |
|Square Bump| (1 - x<sup>2</sup>) * (1 - y<sup>2</sup>)| <img src="http://dpiner.com/images/SquareBump.jpg"> |
|Hyperboloid| sqrt(x<sup>2</sup> + y<sup>2</sup> + c<sup>2</sup>)) / sqrt(1 + c<sup>2</sup>) - c) | <img src="http://dpiner.com/images/Hyperboloid.jpg"> |
|Trig Product| cos(x<sup>2</sup> * π/2) * cos(y<sup>2</sup> * π/2)) | <img src="http://dpiner.com/images/TrigProduct.jpg">|

## Procedural Lake Generation

Procedural lakes are generated by multiplying an original heightmap by the output of a distance function. The result is a heightmap that gets lower towards the center of the image.

Lakes are set by applying all pixels below a specified height blue.

| Name               | Height | Output                                                      |
|--------------------|--------|-------------------------------------------------------------|
| Original Heightmap | --     | <img src="http://dpiner.com/images/heightmap.jpg">          |
| Distance Squared   | < 35   | <img src="http://dpiner.com/images/DistanceSquared_35.jpg"> |
| Square Bump        | < 25   | <img src="http://dpiner.com/images/SquareBump_25.jpg">      |
| Hyperboloid        | < 25   | <img src="http://dpiner.com/images/Hyperboloid_25.jpg">     |
| Trig Product       | < 15   | <img src="http://dpiner.com/images/TrigProduct_15.jpg">     |
