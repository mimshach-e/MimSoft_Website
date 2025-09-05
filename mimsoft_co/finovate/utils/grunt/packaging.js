/* jshint node:true */
module.exports = function(grunt) {
	'use strict';

	var path = require('path');

	var basedir = path.dirname(grunt.file.findup('Gruntfile.js'));
	var theme_name = grunt.file.readJSON(path.join(basedir, 'package.json')).name;
	var builddir = path.join(basedir, 'build', theme_name);

	var secrets_path = grunt.file.findup('secrets.json');
	var secrets = secrets_path ? require( secrets_path ) : {
		livepath: '',
		ssh_host: '',
		export_api_url: '',
		export_api_key: ''
	};

	function exportApiCall(action, callback) {
		var http = require('https');
		var url = secrets.export_api_url + secrets.export_api_key + '/' + action;

		grunt.log.writeln( url );

		http.get(url, function(res) {
			var body = '';

			res.on('data', function(chunk) {
				body += chunk;
			});

			res.on('end', function() {
				var response = body;

				if ( res.headers['content-type'].match( /json/ ) ) {

					// Actions that shouldn't JSON.parse() the response.
					const noParseActions = [
						'elementor-settings',
					];

					if ( noParseActions.includes( action ) ) {
						let validJSON;
						try {
							/*
								Check that we have valid json response but not assign
								to response as JSON.parse() re-orders numeric keys
								and some actions need to ensure the key order mirrors the server's.
							*/
							validJSON = JSON.parse(body.trim());
						} catch(e) {}

						if ( 'error' in validJSON ) {
							return callback( validJSON.error );
						}
					} else {
						try {
							response = JSON.parse(body.trim());
						} catch(e) {}

						if ( 'error' in response ) {
							return callback( response.error );
						}
					}
				}

				callback(null, response);
			});
		}).on('error', function(err) {
			callback(err);
		});
	}

	grunt.registerTask('download-revslider', function() {
		var done = this.async();

		exportApiCall('revslider', function(err, res) {
			if(err) return done(grunt.util.error("API error:"+err));

			if ( res.length === 0 ) {
				done( grunt.util.error( 'No sliders found, possibly something went wrong.' ) );

				console.error( res );

				return;
			}

			var exec = require('child_process').exec;

			var localdir = path.join(builddir, 'samples/revslider/');
			grunt.file.mkdir(localdir);

			var ri = -1;

			var next = function() {
				if(++ri >= res.length)
					return done();

				grunt.log.writeln('Downloading '+res[ri]);

				var url = secrets.export_api_url + secrets.export_api_key + '/revslider-single/' + res[ri];

				var curl = "curl -o '" + path.join(localdir, res[ri] + '.zip') + "' '" + url + "'";

				exec(curl, function(error) {
					if(error) return done(grunt.util.error(error));

					next();
				});
			};

			next();
		});
	});

	grunt.registerTask('download-elementor-styles', function() {
		var done = this.async();

		exportApiCall( 'elementor-styles-fallback', function(err, res) {
			if ( err ) {
				done( grunt.util.error("API error: " + err ) );
				return;
			}

			var css_path = path.join(builddir, 'samples/elementor-styles-fallback.css');

			res.css = res.css.replace( /(.*-line-height.*)em;/g, '$1;' );

			grunt.file.write( css_path, res.css );

			var gfonts_path = path.join(builddir, 'samples/elementor-styles-fallback-fonts.php');

			grunt.file.write( gfonts_path, res.fonts );

			done();
		});
	});

	grunt.registerTask('download-elementor-global-defaults', function() {
		var done = this.async();

		exportApiCall( 'elementor-global-defaults', function(err, res) {
			if ( err ) {
				done( grunt.util.error("API error: " + err ) );
				return;
			}

			var export_path = path.join(builddir, 'samples/elementor-global-defaults.php');

			grunt.file.write( export_path, res.exported );

			done();
		});
	});

	grunt.registerTask('download-json', function( name ) {
		var done = this.async();

		exportApiCall( name, function(err, res) {
			if ( err ) {
				done( grunt.util.error("API error: " + err ) );
				return;
			}

			var exec = require('child_process').exec;

			var localpath = path.join(builddir, 'samples/', name + '.json');

			if ( typeof res !== 'string' ) {
				res = JSON.stringify( res );
			}

			grunt.file.write( localpath, res );

			done();
		});
	});

	grunt.registerTask('download-json-serialized', function( name ) {
		var done = this.async();

		exportApiCall( name, function(err, res) {
			if ( err ) {
				done( grunt.util.error("API error: " + err ) );
				return;
			}

			var exec = require('child_process').exec;

			var localpath = path.join(builddir, 'samples/', name + '.ser.json');

			if ( typeof res !== 'string' ) {
				res = JSON.stringify( res );
			}

			grunt.file.write( localpath, res );

			done();
		});
	});

	grunt.registerTask('check-api', function() {
		var done = this.async();

		exportApiCall('api-version', function(err, res) {
			if(err) return done(false);
			if(!('version' in res) || res.version < grunt.config('pkg').vamtamApi)
				return done(grunt.util.error("Old Export API. Please update the plugin to version " + grunt.config('pkg').vamtamApi));

			done();
		});
	});

	grunt.registerTask('download-sidebars-options', function() {
		var done = this.async();

		var parts = [
			['default-options-beaver', 'default-options.php', 'options'],
		], pi = -1;

		var next = function() {
			if(++pi >= parts.length)
				return done();

			grunt.log.writeln('Downloading '+parts[pi][1]);

			exportApiCall(parts[pi][0], function(err, res) {
				if(err) return done(false);

				if ( typeof res === 'string' ) {
					res = JSON.parse( res );
				}

				grunt.file.write(path.join(builddir, "samples", parts[pi][1]), res[parts[pi][2]].replace(/(\r\n|\r|\n)/g, "\n"));
				next();
			});
		};

		next();
	});

	grunt.registerTask('download-content-xml', function() {
		var done = this.async();

		exportApiCall('content.xml-beaver', function(err, res) {
			if(err) return done(grunt.util.error("API error:"+err));

			console.log(res);

			var exec = require('child_process').exec;
			var curl = "curl --fail-with-body -o "+path.join(builddir, 'samples', 'content.xml')+" "+res.download_url;

			exec(curl, function(err) {
				if(err) return done(grunt.util.error(err));

				grunt.log.writeln("saved content.xml");
				done();
			});
		});
	});

	grunt.registerTask('download-elementor-icons', function() {
		var done = this.async();

		exportApiCall('elementor-icons', function(err, res) {
			if(err) return done(grunt.util.error("API error:"+err));

			console.log(res);

			var exec = require('child_process').exec;
			var curl = "curl -o "+path.join(builddir, 'samples', 'theme-icons.zip') + " " + res.download_url;

			exec(curl, function(err) {
				if(err) return done(grunt.util.error(err));

				grunt.log.writeln( "saved theme-icons.zip" );
				done();
			});
		});
	});

	grunt.registerTask('download-elementor-icons', function() {
		var done = this.async();

		exportApiCall('elementor-icons', function(err, res) {
			if(err) return done(grunt.util.error("API error:"+err));

			console.log(res);

			var exec = require('child_process').exec;
			var curl = "curl --fail-with-body -o "+path.join(builddir, 'samples', 'theme-icons.zip')+" "+res.download_url;

			exec(curl, function(err) {
				if(err) return done(grunt.util.error(err));

				grunt.log.writeln("saved theme-icons.zip");
				done();
			});
		});
	});

	grunt.registerTask('pojo-affiliate-links', function() {
		const done  = this.async();
		const fs    = require('fs');
		const JSZip = require('jszip');

		const zip_path = 'vamtam/plugins/pojo-accessibility.zip';
		const zip = new JSZip();

		fs.readFile( path.join( basedir, zip_path ), function(err, data) {
			if (err) {
				return done(grunt.util.error("Error reading zip file: " + err));
			}

			zip.loadAsync(data).then(function(contents) {
				const file_path = 'pojo-accessibility/assets/build/admin.js';
				const file = contents.file(file_path);

				if ( ! file ) {
					return done(grunt.util.error( "Can't replace affiliate links - file not found" ) );
				}

				file.async('string').then(function(content) {
					content = content.replace(
						'https://go.elementor.com/acc-add-visits',
						'https://be.elementor.com/visit/?bta=13981&nci=5741'
					);

					zip.file(file_path, content);

					zip.generateAsync({ type: 'nodebuffer' }).then(function(newData) {
						fs.writeFile( path.join( builddir, zip_path ), newData, function(err) {
							if (err) {
								return done(grunt.util.error("Error writing zip file: " + err));
							}
							done();
						});
					});
				});
			});
		});
	} );

	grunt.registerMultiTask('add-textdomain', function() {
		var files = grunt.file.expand(this.data);

		for(var fi in files) {
			grunt.file.write(files[fi],
				grunt.file.read(files[fi])
					.replace( /,\s*(['"])(vamtam|wpv)\1/g, ", '"+theme_name+"'")
					.replace( /(load_theme_textdomain|is_textdomain_loaded)\(\s*'(vamtam|wpv)'/g, "$1( '"+theme_name+"'")
			);
		}
	});

    grunt.registerTask('build-plugins', function() {
        grunt.task.run( 'makepot:elements' );

        var done = this.async();
        var prefix = 'vamtam/plugins/';

        var plugins = grunt.file.expand([
            prefix + '*',
            '!' + prefix + '*.*',
        ]);

        plugins.forEach( function( dirname ) {
			var plugin_name = dirname.replace( prefix, '' );
			var js_dir = dirname + '/assets/js/';

			// Gather all JavaScript files in the directory and subdirectories.
			// Exclude any existing .min.js files.
			var js_files = grunt.file.expand({
				filter: 'isFile',
				cwd: js_dir // Set cwd to js_dir.
			}, '**/*.js').filter(function( file ) {
				return ! file.endsWith( '.min.js' ); // Exclude .min.js files.
			});

			// Prepare the Terser configuration.
			if ( js_files.length > 0 ) {
				// Prepare Terser config.
				var terser_config = js_files.map( function( file ) {
					return {
						src: [ js_dir + file ],  // Full path to source file.
						dest: js_dir + file.replace( '.js', '.min.js' ),  // Minified output file.
					};
				});

				// Set up Terser task configuration.
				grunt.config.set( 'terser.plugins_js.files', terser_config.map( function( file ) {
					return {
						src: [ file.src ],  // Ensure src is an array.
						dest: file.dest
					};
				}));

				grunt.config.set( 'terser.plugins_js.options', {
					compress: true, // Enable compression.
					mangle: true,   // Enable name mangling.
					output: {
						comments: false  // Remove comments.
					}
				});

				// Run Terser task for this plugin.
				grunt.task.run( 'terser:plugins_js' );
			}

			// Compress the plugin directory into a zip file.
			grunt.config.set( 'compress.plugin-' + plugin_name, {
				options: {
					archive: prefix + plugin_name + '.zip',
					mode: 'zip',
					pretty: true,
					level: 9,
				},
				files: [{
					expand: true,
					src: [
						plugin_name + '/**/*', // Include all files within the plugin directory.
						'!' + plugin_name + '/node_modules/**', // Exclude node_modules.
					],
					cwd: 'vamtam/plugins/'
				}]
			});

			// Run the compress task for the current plugin.
			grunt.task.run( 'compress:plugin-' + plugin_name );
		});


        done();
    });
};
