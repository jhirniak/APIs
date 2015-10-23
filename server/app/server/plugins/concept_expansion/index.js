/**
 * Created by michael on 23/10/2015.
 */


var watson = require('watson-developer-cloud');


var concept_expansion = watson.concept_expansion({
    username: '678facbe-0318-4120-bdb4-fce3e7a26609',
    password: 'VyGimMKMU0sK',
    version: 'v1'
});



exports.getSimilar = function getSimilar(q, cb){
    var params = {
        seeds: [q],
        dataset: 'social',
        label: 'things'
    };

    concept_expansion.expand(params, function (err, response) {
        if (err) {
            console.log('Watson Concept Expansion:', err);
            cb(err, null);
        }
        else {
            cb(null, {'items': response['return_seeds']})
        }
    });
};
