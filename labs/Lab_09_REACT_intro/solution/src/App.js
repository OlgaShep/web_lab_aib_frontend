import './styles/App.css'
import { useState } from 'react';
import React from 'react';
import Counter from "./components/Counter";
import PostList from "./components/PostList";
import Context from './components/Context'
import PostForm from "./components/PostForm"

function App() {

  const [posts, setPost] = useState([
    {id: 1, fio: "Егор Летов", text: "Гражданская оборона", tag: "#PostPunk"},
    {id: 2, fio: "Игорь Власьев", text: "ЖЩ/Этажность", tag: "#PostPunk"},
    {id: 3, fio: "Андрей Пирокинезис", text: "Pyrokinesis", tag: "#Hip-Hop"},
  ])


  const [tags, setTags] = useState(uniqueTags(posts))

  function uniqueTags(posts) {
    return [...new Set(posts.map(post => post.tag))]
  }

  const deletePost = (delPost) => {
    setPost(posts.filter(post => post.id !== delPost.id))

    if(posts.filter(post => post.tag === delPost.tag).length === 1) {
      setTags(tags.filter(tag => tag !== delPost.tag))
    }
  }

  const addPost = (newPost) => {
    setPost([...posts, {...newPost, id: Date.now()}])
    setTags([...new Set([...tags, newPost.tag])])
  }



  return (
        <>
        <div className='task1'>
          <Counter/>
        </div>

        <p className='delimiter'></p>

        <div className='task234'>
          <PostForm addPost={addPost}/>
          <Context.Provider value={{
          tags,
          setTags
          }}>
            <PostList posts={posts} deletePost={deletePost}/>
          </Context.Provider>
        </div>
        </>
  );
}

export default App;
