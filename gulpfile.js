var gulp = require('gulp'),
    sass = require('gulp-sass'),
    concat = require('gulp-concat'),
    concat_multi = require('gulp-concat-multi'),
    autoprefixer = require('gulp-autoprefixer'),
    rename = require('gulp-rename'),
    cleancss = require('gulp-clean-css'),
    svgstore = require('gulp-svgstore'),
    svgmin = require('gulp-svgmin'),
    minify = require('gulp-minify');


/**
 * CSS
 */
var css_destination = 'frontend/static/css/',
    css_image_destination = 'frontend/static/css/images/',
    js_destination = 'frontend/static/js/',
    css_location = 'frontend/css/',
    scss_location = 'frontend/scss/',
    js_location = 'frontend/js/',
    icon_location = 'frontend/icons/',
    icon_destination = 'frontend/static/svg/',
    libraries_location = 'frontend/libraries/';

// Concat Foundation with custom styles
gulp.task('app-styles', function () {
    return gulp.src(scss_location + '*.scss')
        .pipe(sass({
            'sourcemap=none': true,
            includePaths: [
                'node_modules/foundation-sites/scss'
            ]
        }))
        .pipe(concat('app-styles.css'))
        .pipe(autoprefixer())
        .pipe(gulp.dest(css_destination))
        .pipe(rename('app-styles.min.css'))
        .pipe(cleancss())
        .pipe(gulp.dest(css_destination));
});

// Concat all CSS files to a single one
gulp.task('css-styles', ['app-styles'], function () {
    concat_multi({
            'app.css': css_destination + 'app-styles.min.css',
            'jquery-ui.css': css_destination + 'jquery-ui.css'
        })
        .pipe(cleancss())
        .pipe(gulp.dest(css_destination));
});

/**
 * JS
 */
gulp.task('js-scripts', ['js-libraries'], function () {
    concat_multi({
            'app.js': [
                js_location + 'main.js',
                js_destination + 'jquery.min.js',
                js_destination + 'foundation.js',
                libraries_location + 'svg4everybody/svg4everybody.min.js'
            ],
            'jquery-ui.js': js_destination + 'jquery-ui.js'
        })
        .pipe(minify())
        .pipe(gulp.dest(js_destination));
});

/**
 * SVG
 */
gulp.task('svgstore', function() {
    return gulp.src(icon_location + '*.svg')
        .pipe(svgmin(function() {
            return {
                plugins: [
                    {
                        removeUselessDefs: false
                    },
                    {
                        removeTitle: true
                    }
                ]
            }
        }))
        .pipe(svgstore())
        .pipe(gulp.dest(icon_destination));
});

/**
 * STATIC LIBRARIES
 */
gulp.task('css-libraries', function () {
    gulp.src([
            'node_modules/jquery-ui-bundle/jquery-ui.css'
        ])
        .pipe(gulp.dest(css_destination));
    gulp.src([
            'node_modules/jquery-ui-bundle/images/ui-icons_444444_256x240.png',
            'node_modules/jquery-ui-bundle/images/ui-icons_555555_256x240.png'
        ])
        .pipe(gulp.dest(css_image_destination));
});
gulp.task('js-libraries', function () {
    return gulp.src([
            'node_modules/jquery/dist/jquery.min.js',
            'node_modules/jquery-ui-bundle/jquery-ui.js',
            'node_modules/foundation-sites/dist/js/foundation.js'
        ])
        .pipe(gulp.dest(js_destination));
});


gulp.task('watch', function () {
    gulp.watch(scss_location + '*.scss', ['css']);
    gulp.watch(scss_location + '/*/*.scss', ['css']);
    gulp.watch(js_location + '*.js', ['js-scripts']);
    gulp.watch(icon_location + '*.svg', ['svgstore']);
});


gulp.task('css', ['app-styles', 'css-styles'], function () {});
gulp.task('app', ['css', 'js-scripts', 'svgstore'], function () {});
gulp.task('libraries', ['css-libraries', 'js-libraries'], function () {});
gulp.task('default', ['app', 'libraries'], function () {});
