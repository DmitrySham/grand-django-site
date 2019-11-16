'use strict';

var gulp                   = require('gulp'),
    // sass                   = require('gulp-sass'),
    // changed                = require('gulp-changed'),
    autoprefixer           = require('gulp-autoprefixer'),
    rename                 = require('gulp-rename'),
    // del                    = require('del'),
    concat                 = require('gulp-concat'),
    cssnano                = require('gulp-cssnano'),
    uglify                 = require('gulp-uglify-es').default,
    cache                  = require('gulp-cache'),
    imagemin               = require('gulp-imagemin'),
    imageminJpegRecompress = require('imagemin-jpeg-recompress'),
    pngquant               = require('imagemin-pngquant');
    // browserSync            = require('browser-sync').create();


gulp.task('minCSS', function () {
    return gulp.src([
        './templates/assets/css/bootstrap.min.css',
        './templates/assets/css/font-awesome.css',
        './templates/assets/css/icomoon.css',
        './templates/assets/css/swiper.min.css',
        './templates/assets/css/slider.css',
        './templates/assets/css/animate.css',
        './templates/assets/css/switcher.css',
        './templates/assets/css/owl.carousel.css',
        './templates/assets/css/default.css',
        './templates/assets/css/styles.css',
        './templates/assets/css/main.css',
    ])
        .pipe(autoprefixer([
            "last 1 major version",
            ">= 1%",
            "Chrome >= 45",
            "Firefox >= 38",
            "Edge >= 12",
            "Explorer >= 10",
            "iOS >= 9",
            "Safari >= 9",
            "Android >= 4.4",
            "Opera >= 30"], { cascade: true }))
        .pipe(cssnano())
        .pipe(concat('app.min.css'))
        .pipe(gulp.dest('./templates/assets/dist/'));
});


gulp.task('minJS', function () {
    return gulp.src([
        './templates/assets/js/jquery.min.js',
        './templates/assets/js/popper.min.js',
        './templates/assets/js/bootstrap.min.js',
        './templates/assets/js/owl.carousel.js',
        './templates/assets/js/navigation.js',
        './templates/assets/js/navigation.fixed.js',
        './templates/assets/js/wow.min.js',
        './templates/assets/js/jquery.counterup.min.js',
        './templates/assets/js/waypoints.min.js',
        './templates/assets/js/tabs.min.js',
        './templates/assets/js/jquery.mb.YTPlayer.min.js',
        './templates/assets/js/swiper.min.js',
        './templates/assets/js/isotope.pkgd.min.js',
        './templates/assets/js/switcher.js',
        './templates/assets/js/modernizr.js',
        './templates/assets/js/map.js',
        './templates/assets/js/main.js',
    ])
        .pipe(uglify())
        .pipe(concat('app.min.js'))
        .pipe(gulp.dest('./templates/assets/dist/'));
});


//
// Image minifier - compresses images
//
gulp.task('minIMG', function() {
    return gulp.src('./media/**/*')
        .pipe(cache(imagemin([
            imagemin.gifsicle({interlaced: true}),
            imagemin.jpegtran({progressive: true}),
            imageminJpegRecompress({
                loops: 5,
                min: 65,
                max: 70,
                quality:'medium'
            }),
            imagemin.svgo(),
            imagemin.optipng({optimizationLevel: 3}),
            pngquant({quality: '65-70', speed: 5})
        ],{
            verbose: true
        })))
        .pipe(gulp.dest('./media/'));
});

gulp.task('dist', ['minCSS', 'minJS', 'minIMG']);
