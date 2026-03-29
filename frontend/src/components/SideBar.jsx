import React from 'react'
import sidebarLogo from "../assets/sidebarLogo.jpg";
import '../styles/Sidebar.css'

const SideBar = () => {
  const allChats = [
       {
           id:1,
           chatName: 'This is sample chat 1'
       },
       {
           id:2,
           chatName: 'This is sample chat 2'
       },
       {
           id:3,
           chatName: 'This is sample chat 3'
       }
   ]
  return (
    <div className='sidebar'>
        <div className='logoRow'>
            <img src={sidebarLogo} width={50} height={50}></img>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M6 18 18 6M6 6l12 12" />
            </svg>
        </div>
        <div className='newChat'>
           <p className='text1'>New chat</p>
           <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
               <path strokeLinecap="round" strokeLinejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10" />
           </svg>
        </div>
        <div className='allChats'>
           {allChats.map(chat =>(
               <div key={chat.id} className='chat'>
                   <p className='text1'>{chat.chatName}</p>   
                </div>
           ))}
       </div>
    </div>
  )
}

export default SideBar