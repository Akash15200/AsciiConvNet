const WebDNN = require('webdnn')

// traditional JavaScript version
WebDNN.load('./output')
   .then(function(runner){
       console.log('loaded');

       // add your code here.
       console.log(runner.backendName);

       var x = runner.inputs[0];
       var y = runner.outputs[0];

      // WebDNN.Image.createImageData('/example/data/school_bus.jpg', { dstW: 224, dstH: 224 })
      //    .then(function(array) {
      //        x.set(array);
      //
      //        runner.run()
      //           .then(function() {
      //               console.log('finished');
      //
      //               let y_typed_array = y.toActual();  // convert SymbolicFloat32Array into Float32Array
      //               console.log('Computed vector', y_typed_array);
      //               console.log('Predicted Label', WebDNN.Math.argmax(y_typed_array));
      //
      //           });


         // });

 });
