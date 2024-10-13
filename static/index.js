document.addEventListener('DOMContentLoaded', function () {
    const button1 = document.getElementById('showSection1');
    const button2 = document.getElementById('showSection2');
    const section1 = document.getElementById('section1');
    const section2 = document.getElementById('section2');

    button1.addEventListener('click', function() {
        section1.style.display = 'block';  
        section2.style.display = 'none';   
    });

    button2.addEventListener('click', function() {
        section2.style.display = 'block';  
        section1.style.display = 'none';   
    });
});

document.getElementById('geoForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent form from submitting the traditional way
    
    // Collect form data
    let formData = {
         formType : 'GeoToCart',
         phiDegree : document.getElementById('phiDegree').value,
         phiMin : document.getElementById('phiMin').value,
         phiSec : document.getElementById('phiSec').value,
         lambdaDegree : document.getElementById('lambdaDegree').value,
         phiDirection : document.querySelector('input[name="phiDirection"]:checked').value,
         lambdaMin : document.getElementById('lambdaMin').value,
         lambdaSec : document.getElementById('lambdaSec').value,
         lambdaDirection : document.querySelector('input[name="lambdaDirection"]:checked').value,
         hValue : document.getElementById('hValue').value,
         ellipsoide : document.getElementById('ellipsoidSelect').value
    };
    // Send data to Flask backend using fetch
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('xResult').value = data.X;
        document.getElementById('yResult').value = data.Y;
        document.getElementById('zResult').value = data.Z;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('cartToGeoForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent form from submitting the traditional way
    
    // Collect form data
    let formData = {
         formType : 'CartToGeo',
         xInput : document.getElementById('xInput').value,
         yInput : document.getElementById('yInput').value,
         zInput : document.getElementById('zInput').value,
         ellipsoide : document.getElementById('ellipsoidSelect').value
    };
    // Send data to Flask backend using fetch
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('phiResult').value = data.phiResult;
        document.getElementById('lambdaResult').value = data.lambdaResult;
        document.getElementById('hResult').value = data.hResult;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});



