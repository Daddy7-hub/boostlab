// BoostLab hero: silk-covered devices in a dark studio. Scroll drives the reveal
// via window.__stageP (0..1), set by site.js. Pure three.js, no video assets.
import * as THREE from 'three';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';

const canvas = document.getElementById('scene');
if (canvas) init();

function init() {
  const mobile = matchMedia('(max-width: 640px)').matches;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
  } catch (e) { done(); return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio, mobile ? 1.5 : 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x040405);
  scene.fog = new THREE.Fog(0x040405, 9, 20);
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(renderer), 0.04).texture;
  scene.environmentIntensity = 0.07;

  const camera = new THREE.PerspectiveCamera(mobile ? 46 : 32, 1, 0.1, 60);

  // ---------- light: one hard top spot like a showroom ----------
  const spot = new THREE.SpotLight(0xfff3e6, 520, 26, 0.25, 1.0, 1.7);
  spot.position.set(0.5, 11, -0.6);
  spot.target.position.set(0.5, 0, -0.1);
  spot.castShadow = true;
  spot.shadow.mapSize.set(mobile ? 1024 : 2048, mobile ? 1024 : 2048);
  spot.shadow.bias = -0.0004;
  spot.shadow.radius = 6;
  scene.add(spot, spot.target);
  const rim = new THREE.PointLight(0xd88a4c, 0, 9, 1.4);
  rim.position.set(-2.6, 2.2, -2.8);
  const rim2 = new THREE.PointLight(0xffb27a, 0, 9, 1.4);
  rim2.position.set(3.2, 1.4, -2.2);
  const fill = new THREE.DirectionalLight(0xc9d4ff, 0.35);
  fill.position.set(-6, 2.5, 5);
  scene.add(rim, rim2, fill, new THREE.AmbientLight(0xffffff, 0.02));

  // ---------- light beam + dust ----------
  const beam = new THREE.Mesh(
    new THREE.PlaneGeometry(7.5, 12),
    new THREE.MeshBasicMaterial({ map: beamTex(), transparent: true, opacity: 0.1, depthWrite: false, blending: THREE.AdditiveBlending, fog: false, side: THREE.DoubleSide, depthTest: false })
  );
  beam.position.set(0.5, 5.6, -0.8);
  beam.renderOrder = 10;
  scene.add(beam);
  const DN = mobile ? 250 : 600, dp = new Float32Array(DN * 3);
  for (let i = 0; i < DN; i++) { const r = Math.sqrt(Math.random()) * 2.6, a = Math.random() * 6.283; dp[i * 3] = 0.5 + Math.cos(a) * r; dp[i * 3 + 1] = Math.random() * 6; dp[i * 3 + 2] = -0.5 + Math.sin(a) * r; }
  const dg = new THREE.BufferGeometry(); dg.setAttribute('position', new THREE.BufferAttribute(dp, 3));
  const dustMat = new THREE.PointsMaterial({ color: 0xffe2c4, size: 0.018, transparent: true, opacity: 0.5, depthWrite: false, blending: THREE.AdditiveBlending });
  const dust = new THREE.Points(dg, dustMat);
  dust.position.set(0.5, 0, -0.5); dg.translate(-0.5, 0, 0.5);
  scene.add(dust);

  // ---------- floor ----------
  const floorTex = radialTex(512, [[0, 'rgba(24,23,22,1)'], [0.3, 'rgba(10,10,10,1)'], [1, 'rgba(4,4,5,1)']]);
  const floor = new THREE.Mesh(
    new THREE.CircleGeometry(16, 64),
    new THREE.MeshStandardMaterial({ map: floorTex, roughness: 0.62, metalness: 0.0, envMapIntensity: 0.5 })
  );
  floor.rotation.x = -Math.PI / 2;
  floor.receiveShadow = true;
  scene.add(floor);

  // ---------- laptop ----------
  const alu = new THREE.MeshPhysicalMaterial({ color: 0x1b1b1f, metalness: 0.85, roughness: 0.32, clearcoat: 0.4, clearcoatRoughness: 0.3 });
  const laptop = new THREE.Group();
  const base = new THREE.Mesh(new RoundedBoxGeometry(3.2, 0.12, 2.2, 4, 0.05), alu);
  base.position.y = 0.06;
  base.castShadow = base.receiveShadow = true;
  laptop.add(base);
  const kb = new THREE.Mesh(new THREE.PlaneGeometry(2.7, 1.05), new THREE.MeshStandardMaterial({ map: keyboardTex(), roughness: 0.7, metalness: 0.2 }));
  kb.rotation.x = -Math.PI / 2;
  kb.position.set(0, 0.121, -0.25);
  laptop.add(kb);
  const pad = new THREE.Mesh(new THREE.PlaneGeometry(1.05, 0.6), new THREE.MeshStandardMaterial({ color: 0x232328, roughness: 0.35, metalness: 0.6 }));
  pad.rotation.x = -Math.PI / 2;
  pad.position.set(0, 0.121, 0.6);
  laptop.add(pad);

  const hinge = new THREE.Group();
  hinge.position.set(0, 0.12, -1.08);
  laptop.add(hinge);
  const lid = new THREE.Mesh(new RoundedBoxGeometry(3.2, 2.1, 0.07, 4, 0.04), alu);
  lid.position.set(0, 1.05, -0.035);
  lid.castShadow = true;
  hinge.add(lid);
  hinge.rotation.x = -0.2;

  const ui = makeScreen(1280, 820, drawDashboard);
  const screenMat = new THREE.MeshBasicMaterial({ map: ui.tex, color: 0x000000, toneMapped: false });
  const screen = new THREE.Mesh(new THREE.PlaneGeometry(2.98, 1.9), screenMat);
  screen.position.set(0, 1.06, 0.002);
  hinge.add(screen);
  const glow = new THREE.PointLight(0xffd2a8, 0, 4, 1.5);
  glow.position.set(0, 1.0, 1.3);
  hinge.add(glow);
  scene.add(laptop);

  // ---------- phone ----------
  const phone = new THREE.Group();
  const body = new THREE.Mesh(new RoundedBoxGeometry(0.78, 1.6, 0.08, 6, 0.1), alu);
  body.castShadow = true;
  phone.add(body);
  const pui = makeScreen(400, 820, drawPhone);
  const pMat = new THREE.MeshBasicMaterial({ map: pui.tex, color: 0x000000, toneMapped: false });
  const pScreen = new THREE.Mesh(new THREE.PlaneGeometry(0.7, 1.5), pMat);
  pScreen.position.z = 0.041;
  phone.add(pScreen);
  phone.position.set(2.35, 0.78, 0.15);
  phone.rotation.set(-0.12, -0.38, 0);
  scene.add(phone);
  const stand = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.06, 0.4), alu);
  stand.position.set(2.42, 0.03, 0.32);
  scene.add(stand);

  // ---------- cloth ----------
  const SEG = mobile ? 70 : 110;
  const W = 7.6, D = 5.6, CZ = -0.25;
  const clothGeo = new THREE.PlaneGeometry(W, D, SEG, SEG);
  clothGeo.rotateX(-Math.PI / 2);
  clothGeo.translate(0.35, 0, CZ);
  const pos = clothGeo.attributes.position;
  const N = pos.count;
  const rest = new Float32Array(N * 3);
  const drape = new Float32Array(N * 3);
  const sArr = new Float32Array(N);
  for (let i = 0; i < N; i++) {
    const x = pos.getX(i), z = pos.getZ(i);
    rest[i * 3] = x; rest[i * 3 + 2] = z;
    const h = height(x, z);
    const gx = (height(x + 0.06, z) - height(x - 0.06, z)) / 0.12;
    const gz = (height(x, z + 0.06) - height(x, z - 0.06)) / 0.12;
    const sl = Math.min(1, Math.hypot(gx, gz) * 0.6);
    // folds run down the slope: phase follows the coordinate across the slope
    const across = Math.abs(gx) > Math.abs(gz) ? z : x;
    const fold = Math.sin(across * 6.2 + noise2(x * 0.9, z * 0.9) * 3.0) * 0.6 + noise2(x * 2.6, z * 2.6) * 0.4;
    const pool = h < 0.02 ? 1 : 0;
    const ripple = (Math.sin(Math.hypot(x - 0.2, z + 0.2) * 7 + noise2(x, z) * 4) * 0.5 + 0.5);
    const nx = gx === 0 && gz === 0 ? 0 : -gx / (Math.hypot(gx, gz) || 1), nz = gx === 0 && gz === 0 ? 0 : -gz / (Math.hypot(gx, gz) || 1);
    if (h < 0.02) {
      // skirt: pull toward the object footprint so it bunches instead of lying flat
      const fx = Math.max(-1.75, Math.min(2.8, x)), fz = Math.max(-1.6, Math.min(1.2, z));
      const ox = x - fx, oz = z - fz, od = Math.hypot(ox, oz) || 1;
      const keep = 0.42 + noise2(x * 1.3, z * 1.3) * 0.12;
      const k2 = (od * keep) / od;
      const bx = fx + ox * k2, bz = fz + oz * k2;
      drape[i * 3] = bx; drape[i * 3 + 2] = bz;
      const bunch = Math.max(0, 1 - od * keep / 1.4);
      drape[i * 3 + 1] = 0.006 + (Math.sin(Math.atan2(oz, ox) * 9 + noise2(x, z) * 3) * 0.5 + 0.5) * 0.16 * bunch + ripple * 0.03 * bunch;
      rest[i * 3] = bx; rest[i * 3 + 2] = bz;
      sArr[i] = (bx - (0.35 - W / 2)) / W;
      continue;
    }
    drape[i * 3] = x + nx * fold * 0.11 * sl + Math.sin(x * 4.1 + noise2(x, z * 2) * 2) * 0.05 * Math.min(1, Math.max(0, (Math.abs(gz) - 0.2) * 3));
    drape[i * 3 + 1] = Math.max(0.006 + ripple * 0.07 * pool * Math.max(0, 1 - Math.hypot(x, z) / 4.2), h + fold * 0.06 * sl + Math.sin(x * 4.1 + noise2(x, z * 2) * 2) * 0.09 * Math.min(1, Math.max(0, (-gz - 0.2) * 3)));
    drape[i * 3 + 2] = z + nz * fold * 0.11 * sl;
    sArr[i] = (x - (0.35 - W / 2)) / W; // 0 at left edge
  }
  const silk = new THREE.MeshPhysicalMaterial({
    color: 0xb9ada0, roughness: 0.7, metalness: 0, sheen: 0.8, sheenRoughness: 0.45, sheenColor: new THREE.Color(0xffe8cc),
    side: THREE.DoubleSide, envMapIntensity: 0.5,
  });
  const cloth = new THREE.Mesh(clothGeo, silk);
  cloth.castShadow = true;
  cloth.receiveShadow = true;
  scene.add(cloth);

  function height(x, z) {
    // cloth over the open lid: sags between the top corners, slopes over the keyboard,
    // falls steeply at the sides and back
    const dx = x < -1.62 ? -1.62 - x : x > 1.62 ? x - 1.62 : 0;
    const dz = z + 1.47;
    const u = Math.min(1, Math.max(0, (x + 1.62) / 3.24));
    const sag = Math.sin(u * Math.PI) * (1 - Math.exp(-Math.max(0, dz) * 1.1)) * 0.5;
    const kz = dz > 0 ? 0.8 : 4.5;
    const top = 2.24 - Math.sin(u * Math.PI) * 0.06;
    const hLid = top - Math.hypot(dx * 3.1, dz * kz) - sag;
    const hBase = 0.15 - boxDist(x, z, 1.62, 1.12, 0) * 2.6;
    const px = x < 1.92 ? 1.92 - x : x > 2.78 ? x - 2.78 : 0;
    const hPh = 1.8 - Math.hypot(px * 2.7, (z - 0.12) * 2.4);
    return Math.max(0, smax(smax(hLid, hBase, 0.25), hPh, 0.3));
  }

  let clothState = -1;
  function setCloth(p, t) {
    if (p === clothState && (p <= 0 || p >= 1)) return;
    clothState = p;
    cloth.visible = p < 0.999;
    if (!cloth.visible) return;
    for (let i = 0; i < N; i++) {
      const s = sArr[i];
      let l = THREE.MathUtils.clamp(p * 1.9 - s * 0.9 + (rest[i * 3 + 2] - CZ) * 0.03, 0, 1);
      l = l * l * (3 - 2 * l);
      const zr = rest[i * 3 + 2];
      const wave = Math.sin(t * 3.2 - s * 10 + zr * 1.6) * Math.sin(l * Math.PI);
      const curl = Math.sin(l * Math.PI) * (0.6 + 0.4 * Math.sin(zr * 2.3 + t));
      const x = drape[i * 3] - l * (7.0 + s * 3.0) + wave * 0.25;
      const y = drape[i * 3 + 1] + l * (2.4 + Math.sin(s * 3.1) * 1.6) + wave * 0.55 + curl * 0.5;
      const z = drape[i * 3 + 2] + l * (1.0 - s * 0.9) + Math.cos(t * 2.1 + s * 7) * 0.35 * Math.sin(l * Math.PI);
      pos.setXYZ(i, x, Math.max(y, 0.005), z);
    }
    pos.needsUpdate = true;
    clothGeo.computeVertexNormals();
  }
  setCloth(0, 0);

  // ---------- camera path ----------
  const camFrom = { r: 11.5, a: 0.0, y: 4.4, ty: 0.15 };
  const camMid = { r: 9.6, a: -0.22, y: 3.2, ty: 0.5 };
  const camTo = { r: 7.4, a: -0.62, y: 2.3, ty: 0.75 };
  const mouse = { x: 0, y: 0, sx: 0, sy: 0 };
  addEventListener('pointermove', (e) => { mouse.x = e.clientX / innerWidth - 0.5; mouse.y = e.clientY / innerHeight - 0.5; }, { passive: true });

  function resize() {
    const w = canvas.clientWidth, h = canvas.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    // keep the object framed on portrait screens
    camera.fov = (mobile ? 46 : 32) * (camera.aspect < 1 ? 1.5 : 1);
    camera.updateProjectionMatrix();
  }
  addEventListener('resize', resize);
  resize();

  let sp = 0, visible = true, last = performance.now(), firstFrame = true;
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(canvas);

  // screen labels (.hot-0 laptop, .hot-1 phone) follow their anchors in 3D
  const hots = [document.querySelector('.hot-0'), document.querySelector('.hot-1')];
  const anchors = [[screen, new THREE.Vector3(-1.5, 0.35, 0)], [pScreen, new THREE.Vector3(0.38, 0.55, 0)]];
  const tmp = new THREE.Vector3();
  function placeHots(w, h) {
    anchors.forEach(([obj, local], i) => {
      const el = hots[i]; if (!el) return;
      tmp.copy(local); obj.localToWorld(tmp); tmp.project(camera);
      let x = (tmp.x * 0.5 + 0.5) * w, y = (-tmp.y * 0.5 + 0.5) * h;
      const bw = el.offsetWidth || 220, bh = el.offsetHeight || 60;
      if (i === 0) { x -= bw + 24; y -= bh * 0.5; } else { x += 14; y -= bh * 0.2; }
      x = Math.max(16, Math.min(w - bw - 16, x)); y = Math.max(140, Math.min(h - bh - 16, y));
      el.style.setProperty('--x', x.toFixed(0) + 'px'); el.style.setProperty('--y', y.toFixed(0) + 'px');
    });
  }

  const clock = new THREE.Clock();
  function frame(now) {
    requestAnimationFrame(frame);
    if (!visible && !firstFrame) return;
    const dt = Math.min(0.05, (now - last) / 1000); last = now;
    const t = clock.getElapsedTime();
    const target = reduced ? Math.min(1, (window.__stageP || 0) > 0.05 ? 1 : 0) : (window.__stageP || 0);
    sp += (target - sp) * Math.min(1, dt * 6);

    const pCloth = seg(sp, 0.1, 0.46);
    const pPower = seg(sp, 0.36, 0.56);
    const pOrbit = seg(sp, 0.42, 1.0);
    const pIn = seg(sp, 0.0, 0.42);

    setCloth(pCloth, t);
    phone.visible = stand.visible = pCloth > 0.25;
    laptop.visible = pCloth > 0.02;
    beam.material.opacity = 0.1 + 0.08 * (1 - ease(pPower));
    beam.lookAt(camera.position.x, beam.position.y, camera.position.z);
    dust.rotation.y = t * 0.02;
    dustMat.opacity = 0.55 - 0.25 * pPower;

    // screens power on with a soft flicker
    const flick = pPower > 0 && pPower < 1 ? 0.85 + Math.random() * 0.15 : 1;
    const lv = ease(pPower) * flick;
    screenMat.color.setScalar(lv);
    pMat.color.setScalar(ease(seg(sp, 0.44, 0.62)));
    glow.intensity = lv * 5;
    rim.intensity = ease(seg(sp, 0.3, 0.7)) * 22;
    rim2.intensity = ease(seg(sp, 0.4, 0.8)) * 14;
    ui.draw(t, ease(seg(sp, 0.5, 0.9)));
    pui.draw(t, ease(seg(sp, 0.55, 0.95)));

    // camera
    const a = lerpCam(camFrom, camMid, ease(pIn));
    const c = lerpCam(a, camTo, ease(pOrbit));
    mouse.sx += (mouse.x - mouse.sx) * 0.04; mouse.sy += (mouse.y - mouse.sy) * 0.04;
    const ang = c.a + mouse.sx * 0.12 + Math.sin(t * 0.25) * 0.015;
    camera.position.set(Math.sin(ang) * c.r, c.y - mouse.sy * 0.25, Math.cos(ang) * c.r);
    camera.lookAt(0.25, c.ty, 0);

    const w = canvas.clientWidth, h = canvas.clientHeight;
    const off = camera.aspect > 1.15 ? (1 - ease(seg(sp, 0.08, 0.4))) * 0.24 : 0;
    camera.setViewOffset(w, h, -w * off, h * (camera.aspect > 1.15 ? 0 : 0.22 * (1 - ease(seg(sp, 0.2, 0.6)))), w, h);
    renderer.render(scene, camera);
    if (sp > 0.45 && sp < 0.9) placeHots(w, h);
    if (firstFrame) { firstFrame = false; done(); }
  }
  requestAnimationFrame(frame);
}

// ---------- helpers ----------
function done() { window.dispatchEvent(new Event('scene:ready')); }
function smax(a, b, k) { const h = Math.max(k - Math.abs(a - b), 0) / k; return Math.max(a, b) + h * h * k * 0.25; }
function seg(v, a, b) { return Math.min(1, Math.max(0, (v - a) / (b - a))); }
function ease(v) { return v < 0.5 ? 4 * v * v * v : 1 - Math.pow(-2 * v + 2, 3) / 2; }
function lerpCam(a, b, k) { return { r: a.r + (b.r - a.r) * k, a: a.a + (b.a - a.a) * k, y: a.y + (b.y - a.y) * k, ty: a.ty + (b.ty - a.ty) * k }; }
function segDist(x, z, x0, x1, zc) { const dx = x < x0 ? x0 - x : x > x1 ? x - x1 : 0; const dz = z - zc; return Math.hypot(dx, dz); }
function boxDist(x, z, hx, hz, zc) { const dx = Math.max(0, Math.abs(x) - hx); const dz = Math.max(0, Math.abs(z - zc) - hz); return Math.hypot(dx, dz); }
function noise2(x, y) {
  const h = (a, b) => { const s = Math.sin(a * 127.1 + b * 311.7) * 43758.5453; return s - Math.floor(s); };
  const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
  const u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
  const a = h(xi, yi), b = h(xi + 1, yi), c = h(xi, yi + 1), d = h(xi + 1, yi + 1);
  return (a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v) * 2 - 1;
}
function radialTex(n, stops) {
  const c = document.createElement('canvas'); c.width = c.height = n;
  const g = c.getContext('2d'); const gr = g.createRadialGradient(n / 2, n / 2, 0, n / 2, n / 2, n / 2);
  stops.forEach(([o, col]) => gr.addColorStop(o, col)); g.fillStyle = gr; g.fillRect(0, 0, n, n);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
function beamTex() {
  const c = document.createElement('canvas'); c.width = 256; c.height = 512;
  const g = c.getContext('2d');
  g.filter = 'blur(22px)';
  const gr = g.createLinearGradient(0, 0, 0, 512);
  gr.addColorStop(0, 'rgba(255,238,215,0)'); gr.addColorStop(0.2, 'rgba(255,238,215,.35)'); gr.addColorStop(0.85, 'rgba(255,238,215,.9)'); gr.addColorStop(1, 'rgba(255,238,215,0)');
  g.fillStyle = gr; g.beginPath(); g.moveTo(112, 0); g.lineTo(144, 0); g.lineTo(226, 512); g.lineTo(30, 512); g.closePath(); g.fill();
  return new THREE.CanvasTexture(c);
}
function keyboardTex() {
  const c = document.createElement('canvas'); c.width = 1024; c.height = 400;
  const g = c.getContext('2d'); g.fillStyle = '#141417'; g.fillRect(0, 0, 1024, 400);
  const rows = [14, 14, 13, 12, 11]; let y = 14;
  rows.forEach((n, r) => {
    const kw = (1000 - (n - 1) * 8) / n; let x = 12;
    for (let k = 0; k < n; k++) { g.fillStyle = '#060607'; roundRect(g, x, y, kw, 62, 7); x += kw + 8; }
    y += 76;
  });
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t;
}
function roundRect(g, x, y, w, h, r) { g.beginPath(); g.roundRect(x, y, w, h, r); g.fill(); }
function makeScreen(w, h, painter) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const g = c.getContext('2d');
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  let lastK = -1, lastT = 0;
  return {
    tex, draw(t, k) {
      if (k === lastK && t - lastT < 0.1) return;
      if (k <= 0 && lastK === 0) return;
      lastK = k; lastT = t; painter(g, w, h, t, k); tex.needsUpdate = true;
    },
  };
}

// CRM dashboard painted on the laptop screen
function drawDashboard(g, w, h, t, k) {
  const A = '#D88A4C';
  g.fillStyle = '#0b0b0e'; g.fillRect(0, 0, w, h);
  g.fillStyle = '#101015'; g.fillRect(0, 0, 220, h);
  g.fillStyle = '#ECE8E1'; g.font = '600 26px Unbounded, sans-serif'; g.fillText('BOOST', 32, 62); g.fillStyle = A; g.fillText('LAB', 132, 62);
  ['Dashboard', 'Leads', 'Deals', 'Bookings', 'Invoices', 'Reports'].forEach((s, i) => {
    g.fillStyle = i === 0 ? 'rgba(216,138,76,.16)' : 'transparent'; g.fillRect(16, 110 + i * 56, 188, 42);
    g.fillStyle = i === 0 ? '#F3B47D' : '#8E8A84'; g.font = '500 20px Manrope, sans-serif'; g.fillText(s, 34, 138 + i * 56);
  });
  g.fillStyle = '#ECE8E1'; g.font = '500 30px Unbounded, sans-serif'; g.fillText('Revenue overview', 260, 70);
  g.fillStyle = '#5d5a56'; g.font = '500 18px Manrope, sans-serif'; g.fillText('Live · updated just now', 260, 100);
  const kp = [['Revenue', 48210 * k, '€', '+18%'], ['New leads', 1284 * k, '', '+32%'], ['Conversion', 6.4 * k, '%', '+1.2'], ['Bookings', 312 * k, '', '+9%']];
  kp.forEach((d, i) => {
    const x = 260 + i * 252, y = 130;
    g.strokeStyle = 'rgba(255,255,255,.09)'; g.lineWidth = 2; g.strokeRect(x, y, 236, 120);
    g.fillStyle = '#8E8A84'; g.font = '500 17px Manrope, sans-serif'; g.fillText(d[0], x + 18, y + 34);
    const v = d[1] < 100 ? d[1].toFixed(1) : Math.round(d[1]).toLocaleString('en');
    g.fillStyle = '#ECE8E1'; g.font = '300 38px Unbounded, sans-serif'; g.fillText((d[2] === '€' ? '€' : '') + v + (d[2] === '%' ? '%' : ''), x + 18, y + 86);
    g.fillStyle = '#7fcf8f'; g.font = '600 16px Manrope, sans-serif'; g.fillText(d[3], x + 170, y + 34);
  });
  // chart
  const cx = 260, cy = 290, cw = 640, ch = 300;
  g.strokeStyle = 'rgba(255,255,255,.09)'; g.strokeRect(cx, cy, cw, ch);
  for (let i = 1; i < 4; i++) { g.beginPath(); g.moveTo(cx, cy + i * ch / 4); g.lineTo(cx + cw, cy + i * ch / 4); g.stroke(); }
  const pts = 24, prog = Math.max(0.001, k);
  const yv = (i) => cy + ch - 40 - (Math.sin(i * 0.55) * 0.18 + i / pts * 0.62 + Math.sin(i * 1.7 + 1) * 0.06) * (ch - 70);
  const grad = g.createLinearGradient(0, cy, 0, cy + ch); grad.addColorStop(0, 'rgba(216,138,76,.35)'); grad.addColorStop(1, 'rgba(216,138,76,0)');
  g.beginPath(); g.moveTo(cx + 20, cy + ch);
  const last = Math.floor(pts * prog);
  for (let i = 0; i <= last; i++) g.lineTo(cx + 20 + i * (cw - 40) / pts, yv(i));
  g.lineTo(cx + 20 + last * (cw - 40) / pts, cy + ch); g.closePath(); g.fillStyle = grad; g.fill();
  g.beginPath(); for (let i = 0; i <= last; i++) { const X = cx + 20 + i * (cw - 40) / pts; i ? g.lineTo(X, yv(i)) : g.moveTo(X, yv(i)); }
  g.strokeStyle = A; g.lineWidth = 4; g.stroke();
  if (last > 0) { g.fillStyle = '#F3B47D'; g.beginPath(); g.arc(cx + 20 + last * (cw - 40) / pts, yv(last), 8 + Math.sin(t * 4) * 2, 0, 7); g.fill(); }
  // pipeline
  const px = 920; g.strokeStyle = 'rgba(255,255,255,.09)'; g.strokeRect(px, cy, 332, ch);
  g.fillStyle = '#8E8A84'; g.font = '500 17px Manrope, sans-serif'; g.fillText('Pipeline', px + 18, cy + 34);
  [['New', .92], ['Qualified', .7], ['Proposal', .48], ['Won', .31]].forEach(([n, v], i) => {
    const y = cy + 70 + i * 54; g.fillStyle = '#bdb8b0'; g.fillText(n, px + 18, y);
    g.fillStyle = 'rgba(255,255,255,.06)'; g.fillRect(px + 18, y + 12, 290, 10);
    g.fillStyle = i === 3 ? '#7fcf8f' : A; g.fillRect(px + 18, y + 12, 290 * v * k, 10);
  });
  // rows
  const names = ['Nordic Dental OÜ', 'Kalev Logistics', 'Pirita Rent', 'AFTER Events', 'Baltic Build AS'];
  names.forEach((n, i) => {
    const y = 630 + i * 38; g.fillStyle = i % 2 ? 'transparent' : 'rgba(255,255,255,.025)'; g.fillRect(260, y - 24, 992, 36);
    g.fillStyle = '#bdb8b0'; g.font = '500 17px Manrope, sans-serif'; g.fillText(n, 276, y);
    g.fillStyle = '#5d5a56'; g.fillText(['Deal', 'Lead', 'Booking', 'Invoice', 'Deal'][i], 640, y);
    g.fillStyle = i < Math.round(k * 5) ? '#9fe0ab' : '#F3B47D'; g.fillText(i < Math.round(k * 5) ? 'Synced' : 'Pending', 1100, y);
  });
}

// booking app painted on the phone
function drawPhone(g, w, h, t, k) {
  g.fillStyle = '#0b0b0e'; g.fillRect(0, 0, w, h);
  g.fillStyle = '#ECE8E1'; g.font = '500 30px Unbounded, sans-serif'; g.fillText('Book', 30, 90);
  g.fillStyle = '#8E8A84'; g.font = '500 18px Manrope, sans-serif'; g.fillText('Available today', 30, 124);
  for (let i = 0; i < 4; i++) {
    const y = 160 + i * 150;
    g.fillStyle = '#131318'; g.fillRect(24, y, w - 48, 130);
    const gr = g.createLinearGradient(24, y, 140, y + 130); gr.addColorStop(0, '#3a2a1e'); gr.addColorStop(1, '#D88A4C');
    g.fillStyle = gr; g.fillRect(36, y + 14, 100, 102);
    g.fillStyle = '#ECE8E1'; g.font = '600 20px Manrope, sans-serif'; g.fillText(['Tesla Model 3', 'VIP table #4', 'Studio loft', 'Volvo XC60'][i], 152, y + 44);
    g.fillStyle = '#8E8A84'; g.font = '500 16px Manrope, sans-serif'; g.fillText(['€59 / day', '€240 / night', '€85 / night', '€64 / day'][i], 152, y + 74);
    g.fillStyle = i < Math.round(k * 4) ? '#D88A4C' : 'rgba(255,255,255,.1)'; g.fillRect(152, y + 92, 90, 26);
    g.fillStyle = '#000'; g.font = '700 13px Manrope, sans-serif'; g.fillText('BOOK', 176, y + 110);
  }
  g.fillStyle = '#D88A4C'; g.fillRect(24, h - 90, w - 48, 58);
  g.fillStyle = '#0a0a0a'; g.font = '700 18px Manrope, sans-serif'; g.fillText('Confirm · Pay', w / 2 - 62, h - 54);
}
