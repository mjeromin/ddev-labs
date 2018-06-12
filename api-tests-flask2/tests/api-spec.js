var request = require('request');
var base_url = "http://api:8000/";

describe("When testing api root", function(){
    it("should respond with description", function(done){
        request(base_url, function(error, response, body){
            expect(body).toEqual("Prime API!");
            done();
        });
    });

    it("should respond with status 200", function(done){
        request(base_url + "prime/7", function(error, response, body){
            expect(response.statusCode).toEqual(200);
            console.log(body);
            done();
        });
    });

    it("should confirm prime numbers", function(done){
        request(base_url + "prime/7", function(error, response, body){
            expect(body).toEqual("This is prime: 7\n");
            console.log(body);
            done();
        });
    });
});
