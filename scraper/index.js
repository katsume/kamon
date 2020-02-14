const fs= require('fs')
const url= require('url')
const path= require('path')

const program= require('commander')
const cheerio= require('cheerio')
const rp= require('request-promise')

program
	.option('--base <url>', '', 'http://www.morisige.com/html/hina/tabi/japanese/kamon-hyou-top.html')
	.option('--dst <path>', 'Save images here', process.cwd())
	.parse(process.argv)

;(async ()=>{

	const pages= []
	const images= []

	try {
		const data= await rp(program.base)
		const $= cheerio.load(data)
		$('a[href*="kamon"]').each((i, elm)=>{
			const href= new URL($(elm).attr('href'), program.base)
			pages.push(href.toString())
		})
	} catch(err) {
		console.log(err)
	}

	for(let i=0; i<pages.length; i++){
		try {
			const page= pages[i]
			const data= await rp(page)
			const $= cheerio.load(data)
			const src= new URL($('img').attr('src'), page)
			images.push(src.toString())
		} catch(err) {
			console.log(err)
		}
	}

	if(!fs.existsSync(program.dst)){
		fs.mkdirSync(program.dst)
	}
	for(let i=0; i<images.length; i++){
		try {
			const uri= images[i]
			const basename= path.basename(uri)
			const res= await rp.get({
				uri: uri,
				encoding: null
			})
			const buf= Buffer.from(res)
			fs.writeFileSync(path.join(program.dst, basename), buf)
		} catch(err) {
			console.log(err)
		}
	}

})()
