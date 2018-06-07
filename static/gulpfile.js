var gulp         = require('gulp');
var path         = require('path');
var sass         = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var sourcemaps   = require('gulp-sourcemaps');
var open         = require('gulp-open');

var Paths = {
  HERE                 : './',
  DIST                 : 'dist/',
  CSS                  : './assets/css/',
  SCSS_TOOLKIT_SOURCES : './assets/scss/material-dashboard.scss',
  SCSS                 : './assets/scss/**/**'
};

<<<<<<< HEAD
gulp.task('compile-scss', function () {
  return gulp.src(Paths.SCSS_TOOLKIT_SOURCES)
    .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer())
    .pipe(sourcemaps.write(Paths.HERE))
    .pipe(gulp.dest(Paths.CSS));
=======

var gulp = require('gulp'),
	postcss     = require('gulp-postcss'),
	sourcemaps 	= require('gulp-sourcemaps'),
	autoprefixer= require('gulp-autoprefixer'),
	sass = require('gulp-ruby-sass'),
    notify = require("gulp-notify"),
    sourcemaps = require('gulp-sourcemaps'),

	path = {
    	scss: './scss/style.scss',
    	css: './css/',
    };

gulp.task('css', function() {
    return  sass(path.scss,{style: 'compressed',sourcemap: true})
    		.pipe(sourcemaps.write())
			// for file sourcemaps
			.pipe(sourcemaps.write(path.css))
	        .pipe(gulp.dest(path.css))
>>>>>>> 178cbb66ebac3636a45192965132a47fa5935b2c
});

gulp.task('watch', function () {
  gulp.watch(Paths.SCSS, ['compile-scss']);
});
<<<<<<< HEAD

gulp.task('open', function(){
  gulp.src('./examples/dashboard.html')
  .pipe(open());
=======
 
gulp.task('css:w', function() {
    gulp.watch('./scss/**/*.scss', ['css']);
>>>>>>> 178cbb66ebac3636a45192965132a47fa5935b2c
});

gulp.task('open-app', ['open', 'watch']);
