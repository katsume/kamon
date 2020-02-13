const fs= require('fs')
const url= require('url')

const axios= require('axios')
const cheerio= require('cheerio')

;(async ()=>{

	const pages= []

	try {
		const base= 'http://www.morisige.com/html/hina/tabi/japanese/kamon-hyou-top.html'
		const {data}= await axios.get(base)
		const $= cheerio.load(data)
		$('a[href*="kamon"]').each((i, elm)=>{
			const href= new URL($(elm).attr('href'), base)
			pages.push(href.toString())
		})

	} catch(err) {
		console.log(err)
	}

	for(let i=0; i<pages.length; i++){
		try {
			const page= pages[i]
			const {data}= await axios.get(page)
			const $= cheerio.load(data)
			const src= new URL($('img').attr('src'), page)
			process.stdout.write(src.toString()+'\n')
		} catch(err) {
			console.log(err)
		}
	}

})()
