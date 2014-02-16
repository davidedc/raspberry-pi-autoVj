precision mediump float;

varying vec2 texcoordout;
varying float dist;

uniform sampler2D tex0;
uniform vec3 unib[4];
//uniform float blend ====> unib[0][2]
uniform vec3 unif[20];
//uniform vec3 fogshade ==> unif[4]
//uniform float fogdist ==> unif[5][0]
//uniform float fogalpha => unif[5][1]

void main(void) {
  float ri =  unif[16][0];
  float gi =  unif[16][1];
  float bi =  unif[16][2];
  float rf =  unif[17][0];
  float gf =  unif[17][1];
  float bf =  unif[17][2];
  float dotsCount =  unif[18][0];
  vec2 uv = texcoordout;
  float f = smoothstep(0.0,1.0,uv.y);
  //gl_FragColor = vec4(f,f,f,1.0); // ------ combine using factors

  //float ffact = smoothstep(unif[5][0]/3.0, unif[5][0], dist); // ------ smoothly increase fog between 1/3 and full fogdist
  //gl_FragColor = texc ; // ------ combine using factors



	float time = 1.0;
	vec2 mouse = vec2(1.0,1.0);
	vec2 resolution = vec2(1.0,1.0);
	vec2 p = ( texcoordout.xy  )  * dotsCount;
	p.x *= (resolution.x / resolution.y);
	//Write your Code here (Begin)
	
	
	vec3 col = vec3(smoothstep(0.37, 0.35, length(fract(p.xy) - 0.5)));
	
    vec4 texc = vec4(col.r*ri + (1.0-col.r)*rf,col.g*gi + (1.0-col.g)*gf,col.b*bi + (1.0-col.b)*bf,1.0); // ------ material or basic colour from texture
	
  if (texc.a < unib[0][2]) discard; // ------ to allow rendering behind the transparent parts of this object
	
	gl_FragColor = vec4( texc );
	
	


}


