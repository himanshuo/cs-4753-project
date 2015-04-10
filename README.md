<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">
	<title></title>
	<meta name="generator" content="LibreOffice 4.2.7.2 (Linux)">
	<meta name="created" content="0;0">
	<meta name="changed" content="20150410;195210820326439">
	<style type="text/css">
	<!--
		p { color: #000000 }
		h1 { color: #000000 }
	-->
	</style>
</head>
<body lang="en-US" text="#000000" dir="ltr" style="background: transparent">
<p># cs-4753-project cs 4753 project 
</p>
<h1>Setup Instructions:</h1>
<ol>
	<li><p style="margin-bottom: 0in">Setup the appropriate virtual
	environment 
	</p>
	<ul>
		<li><p style="margin-bottom: 0in">virtualenv -p python3 shopsmart 
		</p>
		<li><p style="margin-bottom: 0in">source /shopsmart/bin/activate 
		</p>
		<li><p style="margin-bottom: 0in">pip install Django==1.7.5</p>
	</ul>
	<li><p style="margin-bottom: 0in">Create the directory you want
	ShopSmart to go in</p>
	<li><p style="margin-bottom: 0in">Clone the github repo</p>
	<ul>
		<li><p style="margin-bottom: 0in">git clone
		https://github.com/himanshuo/cs-4753-project.git</p>
	</ul>
	<li><p style="margin-bottom: 0in">Run the server on localhost</p>
	<ul>
		<li><p style="margin-bottom: 0in">python manage.py runserver</p>
	</ul>
	<li><p>View on your browser</p>
	<ul>
		<li><p><b>IMPORTANT: </b><span style="font-weight: normal">First go
		to localhost:8080/add_stuff. This </span><span style="font-weight: normal">hidden
		page </span><span style="font-weight: normal">will upload the
		products list onto the website. We will eventually configure the
		admin pages to do this instead.</span></p>
		<li><p><span style="font-weight: normal">Run localhost:8080</span></p>
	</ul>
</ol>
<p><br><br>
</p>
<h1>Project Requirements:</h1>
<ol>
	<li value="1"><p style="margin-bottom: 0in">Landing page</p>
	<ul>
		<li><p style="margin-bottom: 0in">Sign up via email address</p>
		<li><p style="margin-bottom: 0in">Future features:</p>
		<ul>
			<li><p style="margin-bottom: 0in">A learn more pop up</p>
			<li><p style="margin-bottom: 0in">Different mobile vs website
			appearances</p>
		</ul>
	</ul>
	<li><p style="margin-bottom: 0in">Home page</p>
	<ul>
		<li><p style="margin-bottom: 0in">Will know if user is a new user
		or previous customer</p>
		<li><p style="margin-bottom: 0in">Shows products that were recently
		looked at</p>
	</ul>
	<li><p style="margin-bottom: 0in">Product Lookup page</p>
	<ul>
		<li><p style="margin-bottom: 0in">Shows all products that are
		currently in the store database</p>
		<li><p style="margin-bottom: 0in">Can click on product name to
		bring to price matching tool</p>
		<li><p style="margin-bottom: 0in">Future features:</p>
		<ul>
			<li><p style="margin-bottom: 0in">Better UI to match coupons with
			products</p>
			<li><p style="margin-bottom: 0in">A search bar for easier access
			to certain products</p>
		</ul>
	</ul>
	<li><p style="margin-bottom: 0in">Price Matching page</p>
	<ul>
		<li><p style="margin-bottom: 0in">Future features:</p>
		<ul>
			<li><p style="margin-bottom: 0in">Use external API to bring in
			prices from other sources</p>
			<li><p style="margin-bottom: 0in">Link to lookup a product from
			the product page</p>
		</ul>
	</ul>
	<li><p>Email page</p>
	<ul>
		<li><p><span style="font-weight: normal">Change the user's email
		address</span></p>
	</ul>
</ol>
</body>
</html>