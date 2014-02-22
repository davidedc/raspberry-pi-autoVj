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

  float stripeCount =  unif[18][0];
  float f = fract((uv.x + uv.y) * stripeCount * 0.5);
  f = step(0.5, f);

  gl_FragColor = vec4(mix(rgbf, rgbi, f), 1.0);
  //if (length(gl_FragColor) < 0.25) discard;
}


