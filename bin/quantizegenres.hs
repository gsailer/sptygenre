import Data.Aeson (decode)
import Data.List (groupBy, sort, sortBy)
import Data.Ord
import qualified Data.ByteString.Lazy as B
import System.IO

quantizeGenres genres = reverse . sortBy (comparing snd) . map (\x -> (head x, length x)) . groupBy (\a b -> a == b) . sort $ concat genres

main = do
    genres_raw <- B.readFile "./genres.json"
    let genres = decode genres_raw :: Maybe [[String]]
    output <- openFile "ranked_genres.data" WriteMode
    case genres of 
        Nothing -> putStrLn "Error: json corrupt?"
        Just genres -> hPrint output . quantizeGenres $ genres
    hClose output