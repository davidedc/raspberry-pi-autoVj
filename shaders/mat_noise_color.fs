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
  float rndx = 43253.9873823;
  vec3 rgbi =  unif[16];
  vec3 rgbf =  unif[17];

  float bandCount = 18.0; //unif[18][0] * 32.0 + unif[18][1] * 182.0;
  float rndy = rndx + 1373412.65453 * unif[18][2];
  vec2 p3 = floor(uv * bandCount);
  vec2 p2 = floor(uv * bandCount * 0.5);
  vec2 p1 = floor(uv * bandCount * 0.25);
  vec2 p0 = floor(uv * bandCount * 0.125);

  float col1 = sin(p0.x * rndx) * 0.06666 +
              sin(p1.y * rndy) * 0.133333 +
              sin(p2.x * rndx) * 0.26666 +
              sin(p3.y * rndy) * 0.53335;
  float col2 = sin(p0.y * rndy) * 0.06666 +
              sin(p1.x * rndx) * 0.13333 +
              sin(p2.y * rndy) * 0.26666 +
              sin(p3.x * rndx) * 0.53335;
  vec3 rgbz = mix(rgbi, vec3(1.0 - rgbi.g, 1.0 - rgbi.b, 1.0 - rgbf.r), col1);
  gl_FragColor = vec4(mix(rgbf, rgbz, col2), 1.0);
  if (gl_FragColor.r < 0.0 || gl_FragColor.g < 0.0 || gl_FragColor.b < 0.0) discard;
}


