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
    apiKey: "AIzaSyCfs0yhmR3IHBT1AvksGfZTp0j4etfRY5s",
    authDomain: "shopwashington-e56e1.firebaseapp.com",
    projectId: "shopwashington-e56e1",
    storageBucket: "shopwashington-e56e1.appspot.com",
    messagingSenderId: "828534542162",
    appId: "1:828534542162:web:342d9495c805f37a8ab48b"
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
