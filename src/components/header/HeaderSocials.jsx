import React from 'react'
import {BsLinkedin} from 'react-icons/bs'
import {FaGithub} from 'react-icons/fa'
import {FaStackOverflow} from 'react-icons/fa'

const HeaderSocials = () => {
  return (
    <dov className="header_socials">
        <a href="https://linkedin.com" target="_blank"><BsLinkedin /></a>
        <a href="https://github.com" target="_blank"><FaGithub /></a>
        <a href="https://stackoverflow.com" target="_blank"><FaStackOverflow /></a>
    </dov>
  )
}

export default HeaderSocials