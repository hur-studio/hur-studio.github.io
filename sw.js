// Huurs Studio: Free 11-Surah Taster Offline Service Worker
const CACHE_NAME = 'huurs-free-taster-v3';

const PRECACHE_ASSETS = [
  "./",
  "./index.html",
  "./START_HERE.html",
  "./manifest.json",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./icons/icon.svg",
  "./suites/SURAH_01_AL_FATIHAH_SUITE.html",
  "./suites/SURAH_18_AL_KAHF_SUITE.html",
  "./suites/SURAH_36_YA_SIN_SUITE.html",
  "./suites/SURAH_55_AR_RAHMAN_SUITE.html",
  "./suites/SURAH_56_AL_WAQIAH_SUITE.html",
  "./suites/SURAH_67_AL_MULK_SUITE.html",
  "./suites/SURAH_78_AN_NABA_SUITE.html",
  "./suites/SURAH_93_AD_DUHA_SUITE.html",
  "./suites/SURAH_112_AL_IKHLAS_SUITE.html",
  "./suites/SURAH_113_AL_FALAQ_SUITE.html",
  "./suites/SURAH_114_AN_NAS_SUITE.html"
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE_ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((k) => {
          if (k !== CACHE_NAME) return caches.delete(k);
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  if (!e.request.url.startsWith('http')) return;

  e.respondWith(
    caches.match(e.request, { ignoreSearch: true }).then((cached) => {
      if (cached) return cached;

      const url = new URL(e.request.url);
      const pathname = url.pathname.split('/').pop() || 'index.html';

      return caches.match('./suites/' + pathname).then((suiteMatch) => {
        if (suiteMatch) return suiteMatch;

        return caches.match('./' + pathname).then((rootMatch) => {
          if (rootMatch) return rootMatch;

          return fetch(e.request).then((networkRes) => {
            if (networkRes && networkRes.status === 200) {
              const resClone = networkRes.clone();
              caches.open(CACHE_NAME).then((cache) => cache.put(e.request, resClone));
            }
            return networkRes;
          }).catch(() => {
            if (e.request.mode === 'navigate') {
              return caches.match('./index.html');
            }
          });
        });
      });
    })
  );
});
