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
  float smooth = unif[18][1];
  float ring = unif[18][2];
  //float smooth = 0.2;
  //float ring = -1.3;
  float f = smoothstep(0.0,1.0,uv.y);

  vec2 p = fract(uv * dotsCount) - vec2(0.5);

  float col = smoothstep(0.35999 - smooth, 0.36 + smooth, fract(length(p) * ring));

  gl_FragColor = vec4(mix(rgbf, rgbi, col), 1.0);
}


