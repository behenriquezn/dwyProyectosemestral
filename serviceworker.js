var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilo.css',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(

    fetch(event.request)
    .then((result)=>{
      return caches.open(CACHE_NAME)
      .then(function(c) {
        c.put(event.request.url, result.clone())
        return result;
      })
      
    })
    .catch(function(e){
        return caches.match(event.request)
    })


   
  );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');



var firebaseConfig = {
  apiKey: "AIzaSyADxtPow_hGRgxn2V5N9EYyCV1vQPKsc_c",
  authDomain: "carwashington-76224.firebaseapp.com",
  databaseURL: "https://carwashington-76224.firebaseio.com",
  projectId: "carwashington-76224",
  storageBucket: "carwashington-76224.appspot.com",
  messagingSenderId: "90284256836",
  appId: "1:90284256836:web:1efccbc19366a44ac15611",
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
//////////////////////////////////////////
let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {
  let titulo = payload.notificacion.title
  let opciones = {
      body: payload.notificacion.body,
      icon: payload.notificacion.icon
  }
self.registration.showNotification(titulo, opciones)
})
