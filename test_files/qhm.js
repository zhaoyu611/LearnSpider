(function(){var c={getRaw:function(g){var f=new RegExp("(^| )"+g+"=([^;]*)(;|$)"),h=f.exec(document.cookie);return h?h[2]||null:null},get:function(g){var f=this.getRaw(g);return"string"==typeof f?(f=decodeURIComponent(f),f):null},setRaw:function(h,f,i){i=i||{};var g=i.expires;"number"==typeof i.expires&&(g=new Date,g.setTime(g.getTime()+i.expires)),document.cookie=h+"="+f+"; path=/"+(g?"; expires="+g.toGMTString():"")+(i.domain?"; domain="+i.domain:"")+(i.secure?"; secure":"")},set:function(g,f,h){this.setRaw(g,encodeURIComponent(f),h)},remove:function(g,f){f=f||{},f.expires=new Date(0),this.setRaw(g,"",f)}},a=function(){var g="";try{if(window.wdextcmd){try{g=window.wdextcmd.GetMid()}catch(f){}}else{if(window.external){try{external.GetSID!==undefined&&(g=external.GetMID(external.GetSID(window)))}catch(f){}}}}catch(f){}return g},d=c.get("__qhmid"),b=a();b!==""&&b!==undefined&&c.set("__qhmid",b,{expires:86400000*365*10,domain:".mediav.com"})})();