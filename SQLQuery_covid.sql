SELECT * 
FROM PortfolioProject..covidDeaths$
Where continent is not Null
ORDER BY 3,4

--SELECT * 
--FROM PortfolioProject..covidvaccinations$
--ORDER BY 3,4

Select location,date,total_cases,new_cases,total_deaths,population
From PortfolioProject..covidDeaths$
where continent is not Null
order by 1,2

--Total cases vs Total Deaths
--Shows Likelihood of dying due to COVID
Select location,date,total_cases,new_cases,total_deaths,(total_deaths/total_cases)*100 As Deathpercentage
From PortfolioProject..covidDeaths$
Where location like '%India%'
and continent is not Null
order by 1,2

--Total cases vs Population
--Shows what percentage pf population got COVID
Select location,date,total_cases,population,(total_cases/population)*100 As Infectedpercentage
From PortfolioProject..covidDeaths$
Where location like '%India%'
and continent is not Null
order by 1,2

--Countries with highest Infection rate compared to population
Select location,Max(total_cases) as Highestinfected,population,Max((total_cases/population)*100 ) As Infectedpercentage
From PortfolioProject..covidDeaths$
--Where location like '%India%'
where continent is not Null
Group by population,location
order by Infectedpercentage desc

--Countries with highest Death Count
Select location,Max(cast(total_deaths as int)) as Totaldeathcount
From PortfolioProject..covidDeaths$
where continent is not Null
Group by location 
Order by Totaldeathcount desc

--Continents with highest Death Count
Select continent,Max(cast(total_deaths as int)) as Totaldeathcount
From PortfolioProject..covidDeaths$
where continent is not Null
Group by continent 
Order by Totaldeathcount desc

--Global Numbers

Select Date,Sum(new_cases) as Totalnewcases,Sum(cast(new_deaths as int)) as Totaldeaths,Sum(cast(new_deaths as int))/Sum(new_cases)*100 as DeathPercentage
From PortfolioProject..covidDeaths$
where continent is not Null
Group By date
order by 1,2

Select Sum(new_cases) as Totalnewcases,Sum(cast(new_deaths as int)) as Totaldeaths,Sum(cast(new_deaths as int))/Sum(new_cases)*100 as DeathPercentage
From PortfolioProject..covidDeaths$
where continent is not Null
--Group By date
order by 1,2

--Total Population vs Vaccinations

--Use CTE
With PopvsVac (Continent, Location, Date, Population, Rollingcount_vaccinations, new_vaccinations)
as
(
Select 
dea.continent, dea.location,dea.date,
dea.population,vac.new_vaccinations
,SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location) AS Rollingcount_vaccinations
From PortfolioProject..covidDeaths$ dea
Join PortfolioProject..covidvaccinations$ vac
    ON dea.location = vac.location
    and dea.date = vac.date
Where dea.continent is not Null
)
SELECT *,(Rollingcount_vaccinations/Population)*100
FROM PopvsVac

--TEMP TABLE

DROP TABLE if exists #Vaccinatedpopulationpercent
CREATE TABLE #Vaccinatedpopulationpercent
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
Rollingcount_vaccinations numeric
)

INSERT INTO #Vaccinatedpopulationpercent
Select 
dea.continent, dea.location,dea.date,
dea.population,vac.new_vaccinations
,SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location) AS Rollingcount_vaccinations
From PortfolioProject..covidDeaths$ dea
Join PortfolioProject..covidvaccinations$ vac
    ON dea.location = vac.location
    and dea.date = vac.date
Where dea.continent is not Null

SELECT *,(Rollingcount_vaccinations/Population)*100
FROM #Vaccinatedpopulationpercent

--Creating View to store data for later Visualization

Create View Vaccinatedpopulationpercent 
as
SELECT
dea.continent, dea.location,dea.date,
dea.population,vac.new_vaccinations
,SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location) AS Rollingcount_vaccinations
From PortfolioProject..covidDeaths$ dea
Join PortfolioProject..covidvaccinations$ vac
    ON dea.location = vac.location
    and dea.date = vac.date
Where dea.continent is not Null

SELECT * 
FROM Vaccinatedpopulationpercent






