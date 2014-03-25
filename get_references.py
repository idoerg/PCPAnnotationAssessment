




<!DOCTYPE html>
<html class="  ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>PCPAnnotationAssessment/get_references.py at master · osamajomaa/PCPAnnotationAssessment · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="osamajomaa/PCPAnnotationAssessment" name="twitter:title" /><meta content="PCPAnnotationAssessment - Gene Ontology annotation assessment for proteins using Protein-Citation-Protein network" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/6306993?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/6306993?s=400" property="og:image" /><meta content="osamajomaa/PCPAnnotationAssessment" property="og:title" /><meta content="https://github.com/osamajomaa/PCPAnnotationAssessment" property="og:url" /><meta content="PCPAnnotationAssessment - Gene Ontology annotation assessment for proteins using Protein-Citation-Protein network" property="og:description" />

    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="8635F50B:75FA:7D3A38:5331A166" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://github.global.ssl.fastly.net/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="IvCT/R2JIu+azYMD5vefDgu8vOH7KFfMeDKcQnTyZQ4=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-2714be798e3a1abfcbd49ca563fdfa1c177cd2e9.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-11ee1161f68234125b5e8198b6c00e0409587b77.css" media="all" rel="stylesheet" type="text/css" />
    


        <script crossorigin="anonymous" src="https://github.global.ssl.fastly.net/assets/frameworks-1eb4805d296158ea875ffc5fa959a11f5a3cdf13.js" type="text/javascript"></script>
        <script async="async" crossorigin="anonymous" src="https://github.global.ssl.fastly.net/assets/github-0eb4075decc9810b544396b3366e14fecf793432.js" type="text/javascript"></script>
        
        
      <meta http-equiv="x-pjax-version" content="ec5d8630b4ee3231236cfa8bf8abbf04">

        <link data-pjax-transient rel='permalink' href='/osamajomaa/PCPAnnotationAssessment/blob/e403b00d50edb75ed9bfcc504519e1c1551f7e11/get_references.py'>

  <meta name="description" content="PCPAnnotationAssessment - Gene Ontology annotation assessment for proteins using Protein-Citation-Protein network" />

  <meta content="6306993" name="octolytics-dimension-user_id" /><meta content="osamajomaa" name="octolytics-dimension-user_login" /><meta content="15597322" name="octolytics-dimension-repository_id" /><meta content="osamajomaa/PCPAnnotationAssessment" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="15597322" name="octolytics-dimension-repository_network_root_id" /><meta content="osamajomaa/PCPAnnotationAssessment" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/osamajomaa/PCPAnnotationAssessment/commits/master.atom" rel="alternate" title="Recent Commits to PCPAnnotationAssessment:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fosamajomaa%2FPCPAnnotationAssessment%2Fblob%2Fmaster%2Fget_references.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="osamajomaa/PCPAnnotationAssessment"
      data-branch="master"
      data-sha="4743ecc01d02ba95a215c879ed28c9f1dab08497"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="osamajomaa/PCPAnnotationAssessment" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2Fosamajomaa%2FPCPAnnotationAssessment"
    class="minibutton with-count js-toggler-target star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/osamajomaa/PCPAnnotationAssessment/stargazers">
      0
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fosamajomaa%2FPCPAnnotationAssessment"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/osamajomaa/PCPAnnotationAssessment/network" class="social-count">
        1
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/osamajomaa" class="url fn" itemprop="url" rel="author"><span itemprop="title">osamajomaa</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/osamajomaa/PCPAnnotationAssessment" class="js-current-repository js-repo-home-link">PCPAnnotationAssessment</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/osamajomaa/PCPAnnotationAssessment" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /osamajomaa/PCPAnnotationAssessment">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/osamajomaa/PCPAnnotationAssessment/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /osamajomaa/PCPAnnotationAssessment/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/osamajomaa/PCPAnnotationAssessment/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /osamajomaa/PCPAnnotationAssessment/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped tooltipped-w" aria-label="Wiki">
          <a href="/osamajomaa/PCPAnnotationAssessment/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_wiki /osamajomaa/PCPAnnotationAssessment/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/osamajomaa/PCPAnnotationAssessment/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /osamajomaa/PCPAnnotationAssessment/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/osamajomaa/PCPAnnotationAssessment/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /osamajomaa/PCPAnnotationAssessment/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/osamajomaa/PCPAnnotationAssessment/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /osamajomaa/PCPAnnotationAssessment/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/osamajomaa/PCPAnnotationAssessment.git" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/osamajomaa/PCPAnnotationAssessment.git" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/osamajomaa/PCPAnnotationAssessment" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/osamajomaa/PCPAnnotationAssessment" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



                <a href="/osamajomaa/PCPAnnotationAssessment/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download osamajomaa/PCPAnnotationAssessment as a zip file"
                   title="Download osamajomaa/PCPAnnotationAssessment as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:bfc4e4d7315d41030abfa3b5d21a44f6 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/osamajomaa/PCPAnnotationAssessment/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/osamajomaa/PCPAnnotationAssessment/blob/andy-logger/get_references.py"
                 data-name="andy-logger"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="andy-logger">andy-logger</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/osamajomaa/PCPAnnotationAssessment/blob/master/get_references.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/osamajomaa/PCPAnnotationAssessment" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">PCPAnnotationAssessment</span></a></span></span><span class="separator"> / </span><strong class="final-path">get_references.py</strong> <span aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="get_references.py" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit file-history-tease">
    <img alt="Osama Jomaa" class="main-avatar js-avatar" data-user="6306993" height="24" src="https://avatars1.githubusercontent.com/u/6306993?s=140" width="24" />
    <span class="author"><a href="/osamajomaa" rel="author">osamajomaa</a></span>
    <time class="js-relative-date" data-title-format="YYYY-MM-DD HH:mm:ss" datetime="2014-03-19T14:31:07-04:00" title="2014-03-19 14:31:07">March 19, 2014</time>
    <div class="commit-title">
        <a href="/osamajomaa/PCPAnnotationAssessment/commit/f6a99e95f07d6dbb189c09ffb274cee5673d9e42" class="message" data-pjax="true" title="merging files">merging files</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>3</strong> contributors</a></p>
          <a class="avatar tooltipped tooltipped-s" aria-label="osamajomaa" href="/osamajomaa/PCPAnnotationAssessment/commits/master/get_references.py?author=osamajomaa"><img alt="Osama Jomaa" class=" js-avatar" data-user="6306993" height="20" src="https://avatars1.githubusercontent.com/u/6306993?s=140" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="idoerg" href="/osamajomaa/PCPAnnotationAssessment/commits/master/get_references.py?author=idoerg"><img alt="Iddo Friedberg" class=" js-avatar" data-user="65008" height="20" src="https://avatars1.githubusercontent.com/u/65008?s=140" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="andyoberlin" href="/osamajomaa/PCPAnnotationAssessment/commits/master/get_references.py?author=andyoberlin"><img alt="andyoberlin" class=" js-avatar" data-user="2171733" height="20" src="https://avatars0.githubusercontent.com/u/2171733?s=140" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Osama Jomaa" class=" js-avatar" data-user="6306993" height="24" src="https://avatars1.githubusercontent.com/u/6306993?s=140" width="24" />
            <a href="/osamajomaa">osamajomaa</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Iddo Friedberg" class=" js-avatar" data-user="65008" height="24" src="https://avatars1.githubusercontent.com/u/65008?s=140" width="24" />
            <a href="/idoerg">idoerg</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="andyoberlin" class=" js-avatar" data-user="2171733" height="24" src="https://avatars0.githubusercontent.com/u/2171733?s=140" width="24" />
            <a href="/andyoberlin">andyoberlin</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">executable file</span>
        <span class="meta-divider"></span>
          <span>441 lines (331 sloc)</span>
          <span class="meta-divider"></span>
        <span>15.438 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/osamajomaa/PCPAnnotationAssessment/raw/master/get_references.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/osamajomaa/PCPAnnotationAssessment/blame/master/get_references.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/osamajomaa/PCPAnnotationAssessment/commits/master/get_references.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff tab-size-8">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>

            </td>
            <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">OrderedDict</span></div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">selenium</span> <span class="kn">import</span> <span class="n">webdriver</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">Bio</span> <span class="kn">import</span> <span class="n">Entrez</span> <span class="k">as</span> <span class="n">ez</span></div><div class='line' id='LC5'><span class="kn">from</span> <span class="nn">Bio.UniProt</span> <span class="kn">import</span> <span class="n">GOA</span></div><div class='line' id='LC6'><span class="kn">import</span> <span class="nn">networkx</span> <span class="kn">as</span> <span class="nn">nx</span></div><div class='line' id='LC7'><span class="kn">import</span> <span class="nn">operator</span></div><div class='line' id='LC8'><span class="kn">import</span> <span class="nn">cPickle</span></div><div class='line' id='LC9'><span class="kn">import</span> <span class="nn">pylab</span></div><div class='line' id='LC10'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC11'><br/></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="c"># Logging</span></div><div class='line' id='LC14'><span class="kn">from</span> <span class="nn">log</span> <span class="kn">import</span> <span class="n">Logger</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="c"># Graphic stuff</span></div><div class='line' id='LC17'><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="kn">as</span> <span class="nn">plt</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="n">ez</span><span class="o">.</span><span class="n">email</span> <span class="o">=</span> <span class="s">&quot;jomaao@miamioh.edu&quot;</span> </div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="n">pmid_pmid</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="n">SCOPUS_QUERY_URL</span> <span class="o">=</span> <span class="s">&quot;http://www.scopus.com/search/form.url?display=advanced&amp;clear=t&amp;origin=searchbasic&quot;</span></div><div class='line' id='LC25'><span class="n">DOI_FORMAT</span> <span class="o">=</span> <span class="s">&#39;DOI(&quot;{0}&quot;)&#39;</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="n">CURR_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">realpath</span><span class="p">(</span><span class="n">__file__</span><span class="p">))</span></div><div class='line' id='LC28'><span class="n">CHROMEDRIVER</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">CURR_PATH</span><span class="p">,</span> <span class="s">&quot;Utilities/chromedriver&quot;</span><span class="p">)</span></div><div class='line' id='LC29'><br/></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="k">def</span> <span class="nf">pmids_from_gaf</span><span class="p">(</span><span class="n">gaf_file</span><span class="p">):</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC33'><span class="sd">        Get the papers cited in the Uniprot_GOA file by their PMID and get the GO terms each paper contained.</span></div><div class='line' id='LC34'><span class="sd">        @param unigoa_file: Uniprot_GOA association file in gaf format. </span></div><div class='line' id='LC35'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_go</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">unigoa_file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">gaf_file</span><span class="p">)</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmids</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_prot</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">inrec</span> <span class="ow">in</span> <span class="n">GOA</span><span class="o">.</span><span class="n">gafiterator</span><span class="p">(</span><span class="n">unigoa_file</span><span class="p">):</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">dbref</span> <span class="ow">in</span> <span class="n">inrec</span><span class="p">[</span><span class="s">&#39;DB:Reference&#39;</span><span class="p">]:</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">dbref</span><span class="p">[:</span><span class="mi">4</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;PMID&#39;</span><span class="p">:</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid</span> <span class="o">=</span> <span class="n">dbref</span><span class="p">[</span><span class="mi">5</span><span class="p">:]</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmids</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">pmid</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">pmid_go</span><span class="p">:</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_go</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">inrec</span><span class="p">[</span><span class="s">&#39;GO_ID&#39;</span><span class="p">]]</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">inrec</span><span class="p">[</span><span class="s">&#39;GO_ID&#39;</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">pmid_go</span><span class="p">[</span><span class="n">pmid</span><span class="p">]:</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_go</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">inrec</span><span class="p">[</span><span class="s">&#39;GO_ID&#39;</span><span class="p">])</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">pmid</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">pmid_prot</span><span class="p">:</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_prot</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">inrec</span><span class="p">[</span><span class="s">&#39;DB_Object_ID&#39;</span><span class="p">]]</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">inrec</span><span class="p">[</span><span class="s">&#39;DB_Object_ID&#39;</span><span class="p">]</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">pmid_prot</span><span class="p">[</span><span class="n">pmid</span><span class="p">]:</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_prot</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">inrec</span><span class="p">[</span><span class="s">&#39;DB_Object_ID&#39;</span><span class="p">])</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">pmids</span><span class="o">.</span><span class="n">keys</span><span class="p">()),</span> <span class="n">pmid_go</span><span class="p">,</span> <span class="n">pmid_prot</span></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><span class="k">def</span> <span class="nf">remove_high_throughput_papers</span><span class="p">(</span><span class="n">pmid_go</span><span class="p">,</span> <span class="n">pmid_prot</span><span class="p">,</span> <span class="n">threshold</span><span class="p">):</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC60'><span class="sd">        Remove the high throughput papers according to a threshold</span></div><div class='line' id='LC61'><span class="sd">        @param pmid_go: A dictionary of papers and the GO terms they are annotated to</span></div><div class='line' id='LC62'><span class="sd">        @param pmid_prot: A dictionary of papers and the proteins they contain  </span></div><div class='line' id='LC63'><span class="sd">    &#39;&#39;&#39;</span>    </div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pmid</span> <span class="ow">in</span> <span class="n">pmid_prot</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">pmid_prot</span><span class="p">[</span><span class="n">pmid</span><span class="p">])</span> <span class="o">&gt;=</span> <span class="n">threshold</span><span class="p">):</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">del</span> <span class="n">pmid_go</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">del</span> <span class="n">pmid_prot</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'><span class="k">def</span> <span class="nf">get_network_degrees</span><span class="p">(</span><span class="n">network</span><span class="p">):</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC72'><span class="sd">        Get the degrees of nodes in a EE or ECE network</span></div><div class='line' id='LC73'><span class="sd">        @param network: The network to get calculate the degrees for its nodes</span></div><div class='line' id='LC74'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ent_deg</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">()</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">network</span><span class="o">.</span><span class="n">nodes</span><span class="p">():</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ent_deg</span><span class="p">[</span><span class="n">node</span><span class="p">]</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">network</span><span class="o">.</span><span class="n">neighbors</span><span class="p">(</span><span class="n">node</span><span class="p">))</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ent_deg</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">(</span><span class="nb">sorted</span><span class="p">(</span><span class="n">ent_deg</span><span class="o">.</span><span class="n">iteritems</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="n">operator</span><span class="o">.</span><span class="n">itemgetter</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">))</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ent_deg</span></div><div class='line' id='LC83'><br/></div><div class='line' id='LC84'><span class="k">def</span> <span class="nf">draw_network_degrees</span><span class="p">(</span><span class="n">net_deg</span><span class="p">,</span> <span class="n">path_name</span><span class="p">,</span> <span class="n">xtitle</span><span class="p">,</span> <span class="n">net_name</span><span class="p">,</span> <span class="n">all_nodes</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC86'><span class="sd">        Plot a histogram of the top N nodes having the highest degrees in a network</span></div><div class='line' id='LC87'><span class="sd">        @param net_deg: dictionary of nodes in the network with their corresponding degree</span></div><div class='line' id='LC88'><span class="sd">        @param path_name: the path to store the exported graph image to</span></div><div class='line' id='LC89'><span class="sd">        @param xtitle: the title of the x axis in the graph</span></div><div class='line' id='LC90'><span class="sd">        @param net_name: the network name: EE or ECE</span></div><div class='line' id='LC91'><span class="sd">        @param all_nodes: a flag to determine whether to draw the whole nodes or just the top N </span></div><div class='line' id='LC92'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xaxis</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">net_deg</span><span class="p">)))</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">yaxis</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">net_deg</span><span class="o">.</span><span class="n">values</span><span class="p">())</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xvals</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">net_deg</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">all_nodes</span><span class="p">):</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">xaxis</span><span class="p">,</span> <span class="n">yaxis</span><span class="p">)</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">fill_between</span><span class="p">(</span><span class="n">xaxis</span><span class="p">,</span><span class="n">yaxis</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s">&#39;cyan&#39;</span><span class="p">)</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">visible</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&quot;Degrees of nodes in the &quot;</span> <span class="o">+</span> <span class="n">net_name</span> <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="s">&quot;network&quot;</span><span class="p">)</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">xaxis</span><span class="p">,</span> <span class="n">yaxis</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&#39;center&#39;</span><span class="p">)</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">gcf</span><span class="p">()</span><span class="o">.</span><span class="n">subplots_adjust</span><span class="p">(</span><span class="n">bottom</span><span class="o">=</span><span class="mf">0.25</span><span class="p">)</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">xticks</span><span class="p">(</span><span class="n">xaxis</span><span class="p">,</span> <span class="n">xvals</span><span class="p">,</span> <span class="n">rotation</span><span class="o">=</span><span class="mi">90</span><span class="p">)</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&quot;Top nodes that have the highest degree in the &quot;</span> <span class="o">+</span> <span class="n">net_name</span> <span class="o">+</span> <span class="s">&quot; &quot;</span> <span class="o">+</span> <span class="s">&quot;network&quot;</span><span class="p">)</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="n">xtitle</span><span class="p">)</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s">&#39;Network Degree&#39;</span><span class="p">)</span>        </div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="n">path_name</span><span class="p">)</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pylab</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC119'>&nbsp;</div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC122'><br/></div><div class='line' id='LC123'><span class="k">def</span> <span class="nf">get_entities</span> <span class="p">(</span><span class="n">pmid_ent</span><span class="p">):</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">entities</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pmid</span> <span class="ow">in</span> <span class="n">pmid_ent</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">ent</span> <span class="ow">in</span> <span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">]:</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">entities</span><span class="p">[</span><span class="n">ent</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">entities</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC132'><br/></div><div class='line' id='LC133'><br/></div><div class='line' id='LC134'><span class="k">def</span> <span class="nf">pmid2doi</span><span class="p">(</span><span class="n">pmid_list</span><span class="p">):</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC136'><span class="sd">        Divide the pmid list to 200 sublists and query PubMed database for the dois</span></div><div class='line' id='LC137'><span class="sd">        @param pmid_list: list of pmids to get the dois for.</span></div><div class='line' id='LC138'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">i</span> <span class="o">=</span> <span class="mi">0</span> </div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">j</span> <span class="o">=</span> <span class="mi">200</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_doi</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="p">(</span><span class="n">j</span> <span class="o">&lt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">pmid_list</span><span class="p">)):</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_doi</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">pmid_doi</span><span class="o">.</span><span class="n">items</span><span class="p">())</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">pmid2doi_Helper</span><span class="p">(</span><span class="n">pmid_list</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">j</span><span class="p">])</span><span class="o">.</span><span class="n">items</span><span class="p">()))</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">i</span> <span class="o">=</span> <span class="n">j</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">j</span> <span class="o">+=</span> <span class="mi">200</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">j</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">pmid_list</span><span class="p">)</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_doi</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">pmid_doi</span><span class="o">.</span><span class="n">items</span><span class="p">())</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">pmid2doi_Helper</span><span class="p">(</span><span class="n">pmid_list</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">j</span><span class="p">])</span><span class="o">.</span><span class="n">items</span><span class="p">()))</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">pmid_doi</span></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'><br/></div><div class='line' id='LC152'><span class="k">def</span> <span class="nf">pmid2doi_Helper</span><span class="p">(</span><span class="n">pmid_list</span><span class="p">):</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC154'><span class="sd">        Query PubMed database to get doi for each pmid which are in 200 sublists</span></div><div class='line' id='LC155'><span class="sd">        @param pmid_list: 200-element list of pmids.</span></div><div class='line' id='LC156'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_doi</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">doi</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_str_list</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">pmid_list</span><span class="p">)[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">handle</span> <span class="o">=</span> <span class="n">ez</span><span class="o">.</span><span class="n">efetch</span><span class="p">(</span><span class="s">&quot;pubmed&quot;</span><span class="p">,</span> <span class="nb">id</span><span class="o">=</span><span class="n">pmid_str_list</span><span class="p">,</span> <span class="n">retmode</span><span class="o">=</span><span class="s">&quot;xml&quot;</span><span class="p">)</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pubmed_rec</span> <span class="ow">in</span> <span class="n">ez</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">handle</span><span class="p">):</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">art_id</span> <span class="ow">in</span> <span class="n">pubmed_rec</span><span class="p">[</span><span class="s">&#39;PubmedData&#39;</span><span class="p">][</span><span class="s">&#39;ArticleIdList&#39;</span><span class="p">]:</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">art_id</span><span class="o">.</span><span class="n">attributes</span><span class="p">[</span><span class="s">&#39;IdType&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;doi&#39;</span><span class="p">:</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">doi</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">art_id</span><span class="p">)</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">art_id</span><span class="o">.</span><span class="n">attributes</span><span class="p">[</span><span class="s">&#39;IdType&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;pubmed&#39;</span><span class="p">:</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">art_id</span><span class="p">)</span>        </div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">doi</span> <span class="o">!=</span> <span class="s">&#39;&#39;</span><span class="p">:</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_doi</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span> <span class="o">=</span> <span class="n">doi</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">doi</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">pmid_doi</span></div><div class='line' id='LC173'><br/></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'><span class="k">class</span> <span class="nc">QueryError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC177'><br/></div><div class='line' id='LC178'><span class="k">def</span> <span class="nf">firefox_setup</span><span class="p">():</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fp</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">FirefoxProfile</span><span class="p">()</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fp</span><span class="o">.</span><span class="n">add_extension</span><span class="p">(</span><span class="n">extension</span><span class="o">=</span><span class="s">&#39;Utilities/firebug-1.11.0.xpi&#39;</span><span class="p">)</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fp</span><span class="o">.</span><span class="n">set_preference</span><span class="p">(</span><span class="s">&quot;extensions.firebug.currentVersion&quot;</span><span class="p">,</span> <span class="s">&quot;1.11.0&quot;</span><span class="p">)</span> <span class="c">#Avoid startup screen</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">fp</span></div><div class='line' id='LC184'><br/></div><div class='line' id='LC185'><span class="k">def</span> <span class="nf">get_references</span><span class="p">(</span><span class="n">pmids_dois</span><span class="p">,</span> <span class="n">webBrowser</span><span class="o">=</span><span class="s">&#39;CHROME&#39;</span><span class="p">):</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC187'><span class="sd">        Starts the process of getting references for a list of dois.        </span></div><div class='line' id='LC188'><span class="sd">        @param pmids_dois: Dictionary of pmids and their corresponding dois to search Scopus for their references.</span></div><div class='line' id='LC189'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_refs</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">webBrowser</span> <span class="o">==</span> <span class="s">&quot;CHROME&quot;</span><span class="p">:</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s">&quot;webdriver.chrome.driver&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">CHROMEDRIVER</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">browser</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Chrome</span><span class="p">(</span><span class="n">CHROMEDRIVER</span><span class="p">)</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">webBrowser</span> <span class="o">==</span> <span class="s">&quot;FIREFOX&quot;</span><span class="p">:</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">browser</span> <span class="o">=</span> <span class="n">webdriver</span><span class="o">.</span><span class="n">Firefox</span><span class="p">(</span><span class="n">firefox_profile</span><span class="o">=</span><span class="n">firefox_setup</span><span class="p">())</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;Please choose either FIREFOX or CHROME as your browser&#39;</span><span class="p">)</span></div><div class='line' id='LC200'><br/></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pmid</span><span class="p">,</span> <span class="n">doi</span> <span class="ow">in</span> <span class="n">pmids_dois</span><span class="o">.</span><span class="n">iteritems</span><span class="p">():</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span> <span class="o">=</span> <span class="n">Logger</span><span class="p">(</span><span class="n">pmid</span> <span class="o">+</span> <span class="s">&quot;.log&quot;</span><span class="p">)</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_refs</span><span class="p">[</span><span class="n">pmid</span><span class="p">]</span> <span class="o">=</span> <span class="n">parse_scopus_output</span><span class="p">(</span><span class="n">search</span><span class="p">(</span><span class="n">browser</span><span class="p">,</span> <span class="n">doi</span><span class="p">,</span> <span class="n">logger</span><span class="p">))</span></div><div class='line' id='LC204'><br/></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">browser</span><span class="o">.</span><span class="n">quit</span><span class="p">()</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_pmid</span> <span class="o">=</span> <span class="n">pmid_refs</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fHandler</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;pmid_pmid&quot;</span><span class="p">,</span> <span class="s">&#39;wb&#39;</span><span class="p">)</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">cPickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">pmid_pmid</span><span class="p">,</span> <span class="n">fHandler</span><span class="p">)</span></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fHandler</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC211'><br/></div><div class='line' id='LC212'><span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="n">browser</span><span class="p">,</span> <span class="n">doi</span><span class="p">,</span> <span class="n">logger</span><span class="p">):</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC214'><span class="sd">        Searches one DOI on Scopus and returns a list of references.        </span></div><div class='line' id='LC215'><span class="sd">        @param doi: The DOI to search.</span></div><div class='line' id='LC216'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s">&quot;Entering Scopus at url: &quot;</span> <span class="o">+</span> <span class="n">SCOPUS_QUERY_URL</span><span class="p">)</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">browser</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">SCOPUS_QUERY_URL</span><span class="p">)</span></div><div class='line' id='LC221'><br/></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s">&quot;Searching for DOI: &quot;</span> <span class="o">+</span> <span class="n">doi</span><span class="p">)</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">search_field</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_id</span><span class="p">(</span><span class="s">&quot;searchfield&quot;</span><span class="p">)</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">search_field</span><span class="o">.</span><span class="n">send_keys</span><span class="p">(</span><span class="n">DOI_FORMAT</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">doi</span><span class="p">))</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">search_button</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_class_name</span><span class="p">(</span><span class="s">&quot;searchButton&quot;</span><span class="p">)</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">search_button</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s">&quot;Selecting all results from the query...&quot;</span><span class="p">)</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">selectAll</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_id</span><span class="p">(</span><span class="s">&quot;selectAllTop&quot;</span><span class="p">)</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">selectAll</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">more_button</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_class_name</span><span class="p">(</span><span class="s">&quot;arrowDownMore&quot;</span><span class="p">)</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">more_button</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reference_viewer_anchor</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_xpath</span><span class="p">(</span><span class="s">&#39;//*[@id=&quot;reqMenuList&quot;]/li[1]/a&#39;</span><span class="p">)</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reference_viewer_anchor</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">selectAll</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_id</span><span class="p">(</span><span class="s">&quot;selectAllTop&quot;</span><span class="p">)</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">selectAll</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">export_button</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_id</span><span class="p">(</span><span class="s">&quot;export&quot;</span><span class="p">)</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">export_button</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC244'><br/></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s">&quot;Moving to export screen&quot;</span><span class="p">)</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">format_select</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_css_selector</span><span class="p">(</span><span class="s">&quot;#exportFormat &gt; option[value=TEXT]&quot;</span><span class="p">)</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">format_select</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC250'><br/></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logger</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s">&quot;Specifying PMID option only&quot;</span><span class="p">)</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">output_select</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_css_selector</span><span class="p">(</span><span class="s">&quot;select[name=view] &gt; option[value=SpecifyFields]&quot;</span><span class="p">)</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">output_select</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">uncheck</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_id</span><span class="p">(</span><span class="s">&quot;selectedCitationInformationItemsAll-Export&quot;</span><span class="p">)</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">uncheck</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">check</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_id</span><span class="p">(</span><span class="s">&quot;selectedBibliographicalInformationItems-Export4&quot;</span><span class="p">)</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">check</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">export_button</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_css_selector</span><span class="p">(</span><span class="s">&quot;input[value=Export]&quot;</span><span class="p">)</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">export_button</span><span class="o">.</span><span class="n">click</span><span class="p">()</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pre</span> <span class="o">=</span> <span class="n">browser</span><span class="o">.</span><span class="n">find_element_by_css_selector</span><span class="p">(</span><span class="s">&quot;pre&quot;</span><span class="p">)</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">text</span> <span class="o">=</span> <span class="n">pre</span><span class="o">.</span><span class="n">text</span></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">text</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC270'><br/></div><div class='line' id='LC271'><br/></div><div class='line' id='LC272'><span class="k">def</span> <span class="nf">parse_scopus_output</span><span class="p">(</span><span class="n">scopus_output</span><span class="p">):</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC274'><span class="sd">        Parses the output of the scopus text format.</span></div><div class='line' id='LC275'><span class="sd">        @param scopus_output: the whole text string that Scopus spits out</span></div><div class='line' id='LC276'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">references</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outputFile</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;temp_file&quot;</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outputFile</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">scopus_output</span><span class="p">)</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outputFile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">outputFile</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;temp_file&quot;</span><span class="p">)</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lines</span> <span class="o">=</span> <span class="n">outputFile</span><span class="o">.</span><span class="n">readlines</span><span class="p">()</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">lines</span><span class="p">:</span></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&quot;PUBMED ID:&quot;</span><span class="p">):</span></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">references</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">[</span><span class="mi">11</span><span class="p">:</span><span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="p">)</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>  </div><div class='line' id='LC287'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">references</span></div><div class='line' id='LC288'><br/></div><div class='line' id='LC289'><br/></div><div class='line' id='LC290'><br/></div><div class='line' id='LC291'><br/></div><div class='line' id='LC292'><span class="k">def</span> <span class="nf">create_ece_network</span><span class="p">(</span><span class="n">pmid_pmid</span><span class="p">,</span><span class="n">pmid_ent</span><span class="p">):</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC294'><span class="sd">        Create a One Depth Citation Relationship (1DCR) Entity-Citation-Entity network where nodes are entities and edges </span></div><div class='line' id='LC295'><span class="sd">        are the hidden relationships between two entities that are in two papers where one cites the other.</span></div><div class='line' id='LC296'><span class="sd">        @param pmid_pmid: the dictionary of the paper and their ciations</span></div><div class='line' id='LC297'><span class="sd">        @param pmid_ent: the dictionary of the papers and their entites (in our case protein IDs or GO terms)</span></div><div class='line' id='LC298'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ece</span> <span class="o">=</span> <span class="n">nx</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#ece.add_nodes_from(get_entities(pmid_ent))</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">visited</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pmid</span> <span class="ow">in</span> <span class="n">pmid_ent</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">pmid</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">visited</span><span class="p">:</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">ent</span> <span class="ow">in</span> <span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">]:</span></div><div class='line' id='LC306'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">pmid_pmid</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="n">pmid</span><span class="p">):</span></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">ref_pmid</span> <span class="ow">in</span> <span class="n">pmid_pmid</span><span class="p">[</span><span class="n">pmid</span><span class="p">]:</span></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">pmid_ent</span><span class="o">.</span><span class="n">has_key</span><span class="p">(</span><span class="n">ref_pmid</span><span class="p">)</span> <span class="ow">and</span> <span class="n">ref_pmid</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">visited</span><span class="p">:</span>        </div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">ref_ent</span> <span class="ow">in</span> <span class="n">pmid_ent</span><span class="p">[</span><span class="n">ref_pmid</span><span class="p">]:</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">ece</span><span class="o">.</span><span class="n">has_edge</span><span class="p">(</span><span class="n">ent</span><span class="p">,</span> <span class="n">ref_ent</span><span class="p">):</span></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ece</span><span class="p">[</span><span class="n">ent</span><span class="p">][</span><span class="n">ref_ent</span><span class="p">][</span><span class="s">&#39;co_ocrnce&#39;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ece</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">ent</span><span class="p">,</span> <span class="n">ref_ent</span><span class="p">,</span> <span class="n">co_ocrnce</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">visited</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ref_pmid</span><span class="p">)</span></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">visited</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pmid</span><span class="p">)</span></div><div class='line' id='LC316'><br/></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ece</span></div><div class='line' id='LC318'><br/></div><div class='line' id='LC319'><span class="k">def</span> <span class="nf">create_ee_network</span><span class="p">(</span><span class="n">pmid_ent</span><span class="p">):</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC321'><span class="sd">        Create a Entity-Entity network where nodes are entities and edges </span></div><div class='line' id='LC322'><span class="sd">        are the hidden relationships between two entities that are in the same paper.</span></div><div class='line' id='LC323'><span class="sd">        @param pmid_ent: the dictionary of the papers and their entities (in our case protein IDs or GO terms)</span></div><div class='line' id='LC324'><span class="sd">    &quot;&quot;&quot;</span>    </div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ee</span> <span class="o">=</span> <span class="n">nx</span><span class="o">.</span><span class="n">Graph</span><span class="p">()</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#ee.add_nodes_from(get_entities(pmid_ent))</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">pmid</span> <span class="ow">in</span> <span class="n">pmid_ent</span><span class="p">:</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">n</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">])</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span><span class="n">n</span><span class="p">):</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">ee</span><span class="o">.</span><span class="n">has_edge</span><span class="p">(</span><span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">][</span><span class="n">i</span><span class="p">],</span> <span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">][</span><span class="n">j</span><span class="p">]):</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ee</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">][</span><span class="n">i</span><span class="p">],</span> <span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">][</span><span class="n">j</span><span class="p">],</span> <span class="n">co_ocrnce</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ee</span><span class="p">[</span><span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">][</span><span class="n">i</span><span class="p">]][</span><span class="n">pmid_ent</span><span class="p">[</span><span class="n">pmid</span><span class="p">][</span><span class="n">j</span><span class="p">]][</span><span class="s">&#39;co_ocrnce&#39;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ee</span></div><div class='line' id='LC336'><br/></div><div class='line' id='LC337'><br/></div><div class='line' id='LC338'><span class="k">def</span> <span class="nf">draw_network</span><span class="p">(</span><span class="n">network</span><span class="p">,</span> <span class="n">net_name</span><span class="p">,</span> <span class="n">image_path</span><span class="p">):</span></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC340'><span class="sd">        Draw a network</span></div><div class='line' id='LC341'><span class="sd">        @param network: the network to draw.</span></div><div class='line' id='LC342'><span class="sd">        @param net_name: the name of the network; EE or ECE.</span></div><div class='line' id='LC343'><span class="sd">        @param imag_path: the path to store the exported graph image to.</span></div><div class='line' id='LC344'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC345'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC346'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">net_name</span> <span class="o">==</span> <span class="s">&#39;pp&#39;</span><span class="p">:</span></div><div class='line' id='LC347'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&quot;Protein-Protein Network&quot;</span><span class="p">)</span></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">net_name</span> <span class="o">==</span> <span class="s">&#39;pcp&#39;</span><span class="p">:</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&quot;Protein-Citation-Protein Network&quot;</span><span class="p">)</span></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">net_name</span> <span class="o">==</span> <span class="s">&#39;gg&#39;</span><span class="p">:</span></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&quot;GO-GO Network&quot;</span><span class="p">)</span></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">net_name</span> <span class="o">==</span> <span class="s">&#39;gcg&#39;</span><span class="p">:</span></div><div class='line' id='LC353'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&quot;GO-Citation-GO Network&quot;</span><span class="p">)</span></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC355'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pos</span> <span class="o">=</span> <span class="n">nx</span><span class="o">.</span><span class="n">graphviz_layout</span><span class="p">(</span><span class="n">network</span><span class="p">,</span> <span class="n">prog</span><span class="o">=</span><span class="s">&#39;neato&#39;</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nx</span><span class="o">.</span><span class="n">draw</span><span class="p">(</span><span class="n">network</span><span class="p">,</span><span class="n">pos</span><span class="p">,</span><span class="n">node_size</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span><span class="n">alpha</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span><span class="n">node_color</span><span class="o">=</span><span class="s">&quot;red&quot;</span><span class="p">,</span> <span class="n">with_labels</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">plt</span><span class="o">.</span><span class="n">savefig</span><span class="p">(</span><span class="n">image_path</span><span class="p">)</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">plt</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC362'><br/></div><div class='line' id='LC363'><span class="k">def</span> <span class="nf">remove_high_degree_nodes</span><span class="p">(</span><span class="n">hd_nodes</span><span class="p">,</span> <span class="n">network</span><span class="p">,</span> <span class="n">topx</span><span class="p">):</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC365'><span class="sd">        Remove the N highest degree nodes from a network.</span></div><div class='line' id='LC366'><span class="sd">        @param hd_nodes: the dictionary of nodes and their corresponding degrees.</span></div><div class='line' id='LC367'><span class="sd">        @param network: the network to remove the highest N degree nodes from.</span></div><div class='line' id='LC368'><span class="sd">        @param topx: N; the number of nodes to remove from the network.</span></div><div class='line' id='LC369'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">top_deg</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">(</span><span class="n">hd_nodes</span><span class="o">.</span><span class="n">items</span><span class="p">()[:</span><span class="n">topx</span><span class="p">])</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">top_deg</span><span class="p">:</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">network</span><span class="o">.</span><span class="n">remove_node</span><span class="p">(</span><span class="n">node</span><span class="p">)</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">network</span><span class="o">.</span><span class="n">nodes</span><span class="p">():</span></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">network</span><span class="o">.</span><span class="n">degree</span><span class="p">(</span><span class="n">node</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">network</span><span class="o">.</span><span class="n">remove_node</span><span class="p">(</span><span class="n">node</span><span class="p">)</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC378'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">network</span></div><div class='line' id='LC379'><br/></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC383'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmids</span><span class="p">,</span> <span class="n">pmid_go</span><span class="p">,</span> <span class="n">pmid_prot</span> <span class="o">=</span> <span class="n">pmids_from_gaf</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">CURR_PATH</span><span class="p">,</span><span class="s">&quot;GOA_Files/gene_association.goa_human&quot;</span><span class="p">))</span></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pmid_dois</span> <span class="o">=</span> <span class="n">pmid2doi</span><span class="p">(</span><span class="n">pmids</span><span class="p">)</span>  </div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC389'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">get_references</span><span class="p">(</span><span class="n">pmid_dois</span><span class="p">,</span> <span class="s">&#39;FIREFOX&#39;</span><span class="p">)</span></div><div class='line' id='LC390'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC392'><span class="sd">    print len(pmid_prot)</span></div><div class='line' id='LC393'><span class="sd">    remove_high_throughput_papers(pmid_go, pmid_prot,60)</span></div><div class='line' id='LC394'><span class="sd">    print len(pmid_prot)</span></div><div class='line' id='LC395'><span class="sd">    pmid_pmid = cPickle.load(open(os.path.join(CURR_PATH,&quot;Pickled_Data/pmid_pmid_human&quot;)))</span></div><div class='line' id='LC396'><span class="sd">    </span></div><div class='line' id='LC397'><span class="sd">    </span></div><div class='line' id='LC398'><span class="sd">    #GO Terms</span></div><div class='line' id='LC399'><span class="sd">    gg_net = create_ee_network(pmid_go)</span></div><div class='line' id='LC400'><span class="sd">    draw_network(gg_net, &#39;gg&#39;, os.path.join(CURR_PATH,&quot;gg_net.png&quot;))</span></div><div class='line' id='LC401'><span class="sd">    </span></div><div class='line' id='LC402'><span class="sd">    gcg_net = create_ece_network(pmid_pmid, pmid_go)</span></div><div class='line' id='LC403'><span class="sd">    draw_network(gcg_net, &#39;gcg&#39;, os.path.join(CURR_PATH,&quot;gcg_net.png&quot;))</span></div><div class='line' id='LC404'><span class="sd">    </span></div><div class='line' id='LC405'><span class="sd">    net_deg_gcg = get_network_degrees(gcg_net)</span></div><div class='line' id='LC406'><span class="sd">    draw_network_degrees(OrderedDict(net_deg_gcg.items()[:10]), os.path.join(CURR_PATH,&quot;net_deg_top_gcg.png&quot;), &#39;Go Terms&#39;, &quot;GCG&quot;, False)</span></div><div class='line' id='LC407'><span class="sd">    draw_network_degrees(net_deg_gcg, os.path.join(CURR_PATH,&quot;net_deg_all_gcg.png&quot;), &#39;Go Terms&#39;, &quot;GCG&quot;)</span></div><div class='line' id='LC408'><span class="sd">    </span></div><div class='line' id='LC409'><span class="sd">    net_deg_gg = get_network_degrees(gg_net)</span></div><div class='line' id='LC410'><span class="sd">    draw_network_degrees(OrderedDict(net_deg_gg.items()[:10]), os.path.join(CURR_PATH,&quot;net_deg_top_gg.png&quot;), &#39;Go Terms&#39;, &quot;GG&quot;, False)</span></div><div class='line' id='LC411'><span class="sd">    draw_network_degrees(net_deg_gg, os.path.join(CURR_PATH,&quot;net_deg_all_gg.png&quot;), &#39;Go Terms&#39;, &quot;GG&quot;)</span></div><div class='line' id='LC412'><span class="sd">    </span></div><div class='line' id='LC413'><span class="sd">    gg_nohigh_net = remove_high_degree_nodes(net_deg_gg, gg_net, 10)</span></div><div class='line' id='LC414'><span class="sd">    gcg_nohigh_net = remove_high_degree_nodes(net_deg_gcg, gcg_net, 10)</span></div><div class='line' id='LC415'><span class="sd">    draw_network(gg_nohigh_net, &#39;gg&#39;, os.path.join(CURR_PATH,&quot;gg_nohigh_net.png&quot;))</span></div><div class='line' id='LC416'><span class="sd">    draw_network(gcg_nohigh_net, &#39;gcg&#39;, os.path.join(CURR_PATH,&quot;gcg_nohigh_net.png&quot;))</span></div><div class='line' id='LC417'><span class="sd">    </span></div><div class='line' id='LC418'><span class="sd">    </span></div><div class='line' id='LC419'><span class="sd">    </span></div><div class='line' id='LC420'><span class="sd">    #Poteins</span></div><div class='line' id='LC421'><span class="sd">    pp_net = create_ee_network(pmid_prot)</span></div><div class='line' id='LC422'><span class="sd">    draw_network(pp_net, &#39;pp&#39;, os.path.join(CURR_PATH,&quot;pp_net.png&quot;))</span></div><div class='line' id='LC423'><span class="sd">    </span></div><div class='line' id='LC424'><span class="sd">    pcp_net = create_ece_network(pmid_pmid, pmid_prot)</span></div><div class='line' id='LC425'><span class="sd">    draw_network(pp_net, &#39;pcp&#39;, os.path.join(CURR_PATH,&quot;pcp_net.png&quot;))</span></div><div class='line' id='LC426'><span class="sd">    </span></div><div class='line' id='LC427'><span class="sd">    net_deg_pcp = get_network_degrees(pcp_net)</span></div><div class='line' id='LC428'><span class="sd">    draw_network_degrees(OrderedDict(net_deg_pcp.items()[:10]), os.path.join(CURR_PATH,&quot;net_deg_top_pcp.png&quot;), &#39;Proteins&#39;, &quot;PCP&quot;, False)</span></div><div class='line' id='LC429'><span class="sd">    draw_network_degrees(net_deg_pcp, os.path.join(CURR_PATH,&quot;net_deg_all_pcp.png&quot;), &#39;Proteins&#39;, &quot;PCP&quot;)</span></div><div class='line' id='LC430'><span class="sd">    </span></div><div class='line' id='LC431'><span class="sd">    net_deg_pp = get_network_degrees(pp_net)</span></div><div class='line' id='LC432'><span class="sd">    draw_network_degrees(OrderedDict(net_deg_pp.items()[:10]), os.path.join(CURR_PATH,&quot;net_deg_top_pp.png&quot;), &#39;Proteins&#39;, &quot;PP&quot;, False)</span></div><div class='line' id='LC433'><span class="sd">    draw_network_degrees(net_deg_pp, os.path.join(CURR_PATH,&quot;net_deg_all_pp.png&quot;), &#39;Proteins&#39;, &quot;PP&quot;)</span></div><div class='line' id='LC434'><span class="sd">    </span></div><div class='line' id='LC435'><span class="sd">    pp_nohigh_net = remove_high_degree_nodes(net_deg_pp, pp_net, 10)</span></div><div class='line' id='LC436'><span class="sd">    pcp_nohigh_net = remove_high_degree_nodes(net_deg_pcp, pcp_net, 10)</span></div><div class='line' id='LC437'><span class="sd">    draw_network(pp_nohigh_net, &#39;pp&#39;, os.path.join(CURR_PATH,&quot;pp_nohigh_net.png&quot;))</span></div><div class='line' id='LC438'><span class="sd">    draw_network(pcp_nohigh_net, &#39;pcp&#39;, os.path.join(CURR_PATH,&quot;pcp_nohigh_net.png&quot;))</span></div><div class='line' id='LC439'><span class="sd">    </span></div><div class='line' id='LC440'><span class="sd">&#39;&#39;&#39;</span></div></pre></div></td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.05213s from github-fe125-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

