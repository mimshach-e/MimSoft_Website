<?php

/**
 * Controls attached to core sections
 *
 * @package vamtam/finovate
 */

function vamtam_theme_customize_register( $wp_customize ) {
	global $vamtam_theme;

	$wp_customize->add_setting( 'vamtam_theme[wc-product-gallery-zoom]', array(
		'default'           => $vamtam_theme['wc-product-gallery-zoom'],
		'transport'         => 'refresh',
		'type'              => 'option',
		'sanitize_callback' => function ( $input, $setting ) {
			return ( in_array( $input, [ 'enabled', 'disabled' ] ) ) ? $input : $setting->default;
		}
	) );

	$wp_customize->add_control( 'vamtam_theme[wc-product-gallery-zoom]', array(
		'label'    => esc_html__( 'Single Product Image Zoom', 'finovate' ),
		'section'  => 'woocommerce_product_images',
		'settings' => 'vamtam_theme[wc-product-gallery-zoom]',
		'type'     => 'radio',
		'choices'  => array(
			'enabled'  => esc_html__( 'Enabled', 'finovate' ),
			'disabled' => esc_html__( 'Disabled', 'finovate' ),
		),
	) );
}

add_action( 'customize_register', 'vamtam_theme_customize_register' );

