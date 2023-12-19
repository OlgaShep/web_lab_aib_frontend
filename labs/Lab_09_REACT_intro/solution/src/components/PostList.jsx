import React, { useContext, useState } from "react";
import Post from "./Post";
import Context from '../components/Context'

const PostList = ({posts, deletePost}) => {

    const {tags, setTags} = useContext(Context)
    const [tagsOn, setTagsOn] = useState({
        tagOn: ''
    })

    return (
        <>
            <div className='Grid'>
                <div>
                    {
                    tags.map(tag => 
                        <button 
                        value={tag.includes('#') ? ` ${tag}` : ` #${tag}`}
                        key={tag}
                        onClick={() => {setTagsOn({tagOn: tag})}} style={tagsOn.tagOn === tag ? {color: 'red'} : {color: 'black'}}
                        >
                        {tag.includes('#') ? ` ${tag}` : ` #${tag}`}
                        </button>
                        )
                    }
                </div>
                {posts.sort((a, b) => {
                    return b.tag === tagsOn.tagOn ? 1 : a.tag === tagsOn.tagOn ? -1 : 0;
                    }).map(post => 
                        <Post deletePost={deletePost} post={post} key={post.id}/>)
                    }
            </div>
        </>
    )
}

export default PostList;
