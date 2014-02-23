precision mediump float;

varying vec2 uv;
varying float dist;

uniform sampler2D tex0;
uniform vec3 unib[4];
//uniform float blend ====> unib[0][2]
uniform vec3 unif[20];
//uniform vec3 fogshade ==> unif[4]
//uniform float fogdist ==> unif[5][0]
//uniform float fogalpha => unif[5][1]

void main(void) {
  vec3 rgbi =  unif[16];
  vec3 rgbf =  unif[17];

  float dotsCount =  unif[18][0];
  float petal = unif[18][1];
  float power = unif[18][2];

  vec2 p = fract(uv * dotsCount) - vec2(0.5);

  float col = step(0.36, length(p) * pow(fract((1000.0 + dist) * 0.005 * petal * atan(p.y / p.x)), power));

  gl_FragColor = vec4(mix(rgbf, rgbi, col), 1.0);
  if (gl_FragColor.r < 0.0 || gl_FragColor.g < 0.0 || gl_FragColor.b < 0.0) discard;
}


