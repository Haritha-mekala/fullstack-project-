import { useState } from 'react'


export default function App() {
const [text, setText] = useState('I love this!')
const [result, setResult] = useState(null)
const [hello, setHello] = useState('')


async function ping() {
const r = await fetch('/api/hello')
const data = await r.json()
setHello(data.message)
}


async function analyze() {
const r = await fetch('/api/sentiment', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ text })
})
const data = await r.json()
setResult(data)
}


return (
<div style={{ maxWidth: 720, margin: '2rem auto', fontFamily: 'system-ui' }}>
<h1>AI Sentiment Demo</h1>
<button onClick={ping}>Ping Backend</button>
{hello && <p>Backend says: <b>{hello}</b></p>}
<hr/>
<label>Enter text</label>
<textarea rows="4" style={{ width: '100%' }} value={text} onChange={e => setText(e.target.value)} />
<button onClick={analyze}>Analyze</button>
{result && (
<pre>{JSON.stringify(result, null, 2)}</pre>
)}
</div>
)
}
