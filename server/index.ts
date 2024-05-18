import express from 'express'
const app: express.Express = express()
const port = 3000

let body: any = null;

/**
 * health check
 */
app.get('/', (_req, res) => {
  res.send('Hello World from M5E server!');
})

/**
 * clientに次に実行してもらいたい命令を取得するための口。
 */
app.get('/order', (_req, res) => {
  res.send('Hello World from M5E server!');
})

/**
 * clientが、画像をアップロードする口
 */
app.post('/photo', (req, res) => {
  body = req.body;
  console.log('body: ' + body);
})

/**
 * アップロードした画像を、人間がブラウザから見るための口
 */
app.get('/photo', (req, res) => {
  console.log('body: ' + body);
})


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
})