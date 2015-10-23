"use strict";

var Joi = require('joi'),
    Hoek = require('hoek');

module.exports = function (request, reply) {

  $.ajax({
    url: this.props.url,
    dataType: 'json',
    type: 'POST',
    data: comment,
    success: function (data) {
      this.setState({data: data});
    }.bind(this),
    error: function (xhr, status, err) {
      console.error(this.props.url, status, err.toString());
    }.bind(this)
  });

  var createArticleService = request.server.methods.blog.createArticle,
      opts = {
        action: {
          errors: [],
          status: null
        },
        page: {
          current: 'blogCreate'
        }
      };

  if (request.method === 'post') {

    var schema = Joi.object().keys({
      title: Joi.string().required().label('Title'),
      body: Joi.string().required().label('Body')
    }), joiOptions = {
      convert: false,
      abortEarly: false
    }, data = request.payload;


    Joi.validate(data, schema, joiOptions, function (err, value) {

      if (err) {
        opts.action.errors = err.details;
        return reply.view('blog/create', Hoek.applyToDefaults(opts, {action: {status: 'error'}}));
      }

      createArticleService(value, function (err, article) {
        if (err) {
          opts.action.errors = err.details;
          return reply.view('blog/create', Hoek.applyToDefaults(opts, {action: {status: 'error'}}));
        }
        opts.article = article;
        reply.view('blog/create', Hoek.applyToDefaults(opts,
            {action: {status: 'success', message: 'You successfully posted this article.'}}
        ));
      });
    });
  }

  if (request.method === 'post' || request.method === 'head') {
    return reply.view('experience/fullscreen', experienceData);
  }
};