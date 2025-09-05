<?php

/**
 * Help page
 *
 * @package vamtam/finovate
 */
class VamtamHelpPage {

	public static $mu_plugin_opt_name;

	/**
	 * Actions
	 */
	public function __construct() {
		add_action( 'admin_menu', array( __CLASS__, 'admin_menu' ), 21 );
		add_action( 'admin_init', array( __CLASS__, 'admin_init' ) );
}

	public static function admin_menu() {
		add_submenu_page( 'vamtam_theme_setup', esc_html__( 'Help', 'finovate' ), esc_html__( 'Help', 'finovate' ), 'edit_theme_options', 'vamtam_theme_help', array( __CLASS__, 'page' ) );
	}

	public static function settings_section() {
	}

	public static function admin_init() {
		add_settings_section(
			'vamtam_help_settings_section',
			'',
			array( __CLASS__, 'settings_section' ),
			'vamtam_theme_help'
		);

		add_settings_field(
			'vamtam-system-status-opt-in',
			esc_html__( 'Enable System Status Information Gathering', 'finovate' ),
			array( __CLASS__, 'radio' ),
			'vamtam_theme_help',
			'vamtam_help_settings_section',
			array(
				'vamtam-system-status-opt-in',
				true,
			)
		);

		register_setting(
			'vamtam_theme_help',
			'vamtam-system-status-opt-in'
		);
	}

	public static function page() {
		include VAMTAM_OPTIONS . 'help/docs.php';
	}

	public static function radio( $args ) {
		$value = vamtam_sanitize_bool( get_option( $args[0], $args[1] ) );
?>

		<label><input type="radio" id="<?= esc_attr( $args[0] ) ?>-on" name="<?= esc_attr( $args[0] ) ?>" value="1" <?php checked( $value, true ) ?>/><?php esc_html_e( 'On', 'finovate' ) ?></label>
		<label><input type="radio" id="<?= esc_attr( $args[0] ) ?>-off" name="<?= esc_attr( $args[0] ) ?>" value="0" <?php checked( $value, false ) ?>/><?php esc_html_e( 'Off', 'finovate' ) ?></label>

		<p class="description"><?php
			esc_html_e( 'This option allows us to receive comprehensive data about your site, which can expedite the troubleshooting process, and enable our team to provide you with more accurate and timely assistance. When enabled, we will receive information about the following:', 'finovate' );
			?><br>
			<ol>
				<li><?= wp_kses_post( 'The result of the diagnostic tests shown on the <i>Import Demo</i> page', 'finovate' ) ?></li>
				<li><?php esc_html_e( 'Active plugins and their versions', 'finovate' ) ?></li>
				<li><?php esc_html_e( 'WP_DEBUG', 'finovate' ) ?></li>
			</ol>
		</p>
<?php
	}
}


