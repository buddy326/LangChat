import React, {use, useState} from 'react'
import '../styles/ChatPage.css'

const ChatPage = () => {
  const [input, setInput] = useState("")
  const [messages, setMessages] = useState([])
  
  return (
    <div className='chatpage'>
        <div className='modelRow'>
            <p className='text1'>UniMate</p>
        </div>
        <div className='responsesPage'>

       </div>
        <form className="inputBar">
             <label className="uploadBtn">
                📎
            <input type="file" hidden />
      </label>

      <input
        type="text"
        placeholder="Ask away"
      />
      <button type="submit">➤</button>
    </form>
    </div>
  )
}

export default ChatPage