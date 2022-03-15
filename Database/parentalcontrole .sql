-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 08 fév. 2022 à 01:55
-- Version du serveur : 10.4.22-MariaDB
-- Version de PHP : 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `parentalcontrole`
--

-- --------------------------------------------------------

--
-- Structure de la table `admina`
--

CREATE TABLE `admina` (
  `email` varchar(30) NOT NULL,
  `password` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `admina`
--

INSERT INTO `admina` (`email`, `password`) VALUES
('elazzouzi@gmail.com', '123456'),
('youssef@gmail.com', '123456');

-- --------------------------------------------------------

--
-- Structure de la table `adultea`
--

CREATE TABLE `adultea` (
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `adultea`
--

INSERT INTO `adultea` (`nom`, `prenom`, `age`, `email`) VALUES
('houssni', 'nadia', 24, 'youssef@gmail.com'),
('uuuuuuuu', 'ffff', 44, 'elazzouzi@gmail.com'),
('zerhouni ', 'zineb', 19, 'youssef@gmail.com'),
('l9admiri', 'brahim', 20, 'elazzouzi@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `blackliste`
--

CREATE TABLE `blackliste` (
  `url` varchar(30) DEFAULT NULL,
  `date_d` int(11) DEFAULT NULL,
  `date_f` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `blackliste`
--

INSERT INTO `blackliste` (`url`, `date_d`, `date_f`, `email`) VALUES
('www.facebook.com', 20, 21, 'youssef@gmail.com'),
('www.facebook.com', 20, 21, 'youssef@gmail.com'),
('www.facebook.com', 20, 21, 'youssef@gmail.com'),
('www.facebook.com', 20, 21, 'youssef@gmail.com'),
('www.facebook.com', 20, 21, 'youssef@gmail.com'),
('www.facebook.com', 20, 21, 'youssef@gmail.com'),
('www.facebook.com', 20, 21, 'youssef@gmail.com'),
('www.instagram.com', 20, 21, 'youssef@gmail.com'),
('www.gmail.com', 21, 22, 'youssef@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `filsa`
--

CREATE TABLE `filsa` (
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `filsa`
--

INSERT INTO `filsa` (`nom`, `prenom`, `age`, `email`) VALUES
('lehmachi', 'mohamed', 12, 'youssef@gmail.com'),
('dddd', 'ffff', 12, 'elazzouzi@gmail.com'),
('l9admiri', 'brahim', 15, 'youssef@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `motcle`
--

CREATE TABLE `motcle` (
  `motcle` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `motcle`
--

INSERT INTO `motcle` (`motcle`, `email`) VALUES
('Violence', 'youssef@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `whiteliste`
--

CREATE TABLE `whiteliste` (
  `url` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `whiteliste`
--

INSERT INTO `whiteliste` (`url`, `email`) VALUES
('www.facebook.com', 'youssef@gmail.com'),
('www.instagram.com', 'youssef@gmail.com'),
('www.youtube.com', 'youssef@gmail.com'),
('www.gmail.com', 'youssef@gmail.com'),
('www.facebook.com', 'elazzouzi@gmail.com'),
('www.stackoverflow.com', 'youssef@gmail.com');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `admina`
--
ALTER TABLE `admina`
  ADD PRIMARY KEY (`email`);

--
-- Index pour la table `adultea`
--
ALTER TABLE `adultea`
  ADD KEY `email` (`email`);

--
-- Index pour la table `blackliste`
--
ALTER TABLE `blackliste`
  ADD KEY `email` (`email`);

--
-- Index pour la table `filsa`
--
ALTER TABLE `filsa`
  ADD KEY `email` (`email`);

--
-- Index pour la table `motcle`
--
ALTER TABLE `motcle`
  ADD KEY `email` (`email`);

--
-- Index pour la table `whiteliste`
--
ALTER TABLE `whiteliste`
  ADD KEY `email` (`email`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `adultea`
--
ALTER TABLE `adultea`
  ADD CONSTRAINT `adultea_ibfk_1` FOREIGN KEY (`email`) REFERENCES `admina` (`email`);

--
-- Contraintes pour la table `blackliste`
--
ALTER TABLE `blackliste`
  ADD CONSTRAINT `blackliste_ibfk_1` FOREIGN KEY (`email`) REFERENCES `admina` (`email`);

--
-- Contraintes pour la table `filsa`
--
ALTER TABLE `filsa`
  ADD CONSTRAINT `filsa_ibfk_1` FOREIGN KEY (`email`) REFERENCES `admina` (`email`);

--
-- Contraintes pour la table `motcle`
--
ALTER TABLE `motcle`
  ADD CONSTRAINT `motcle_ibfk_1` FOREIGN KEY (`email`) REFERENCES `admina` (`email`);

--
-- Contraintes pour la table `whiteliste`
--
ALTER TABLE `whiteliste`
  ADD CONSTRAINT `whiteliste_ibfk_1` FOREIGN KEY (`email`) REFERENCES `admina` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
