/*
Copyright (c) 2003-2010, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

CKEDITOR.editorConfig = function( config )
{
    // config.toolbar = 'Basic';
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	config.uiColor = '#417690';
    config.toolbar = 'AdminFormat';
    config.toolbar_AdminFormat =
    [
        ['Cut','Copy','Paste','PasteText','-','Scayt'],
        ['Undo','Redo','-'],
        ['Image','Smiley'],
        ['Styles','Format'],
        ['Bold','Italic','Strike'],
        ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'],
        ['Link','Unlink'],
        ['About']
    ];

};
