// making decision tree with gini method 

#include <fstream>    
#include <string>     
#include <vector>    
#include <sstream>
#include <iostream>
using namespace std;



static vector<string> parseCSVLine(const string& line ){
    // why we use static --> cannot be called form any other file , preventing conflicts (tested)

    vector<string> out;
    string cur;
    bool inQuotes = false;

    for(size_t i = 0; i < line.size() ; ++i){
        char c = line[i];
        if(c == '"'){
            if(inQuotes && i + 1 < line.size() && line[i+1] == '"'){
                cur.push_back('"');
                ++i;
            }else{
                inQuotes != inQuotes;
            }
        }else if(c == ',' && !inQuotes){
            out.push_back(cur);
            cur.clear();
            // what does clear do ---> remove all element form vector making it empty
        }else{
            cur.push_back(c);
        }
    }
    out.push_back(cur);
    return out ;
 }

struct Dataset {
    // why this data set ??
    vector<vector<double>> X;
    vector<double> Y;
    vector<string> feature_name;
};

vector<string> readCsv(){
    ifstream file("data.csv");  // Open CSV file
    string line; // 
    vector<string> row;

    if(!file.is_open()){
        cerr<<"Error : could not open file "<< endl;
        return {};
    }
    else{
        cout<<"was able to open file "<< endl;
        
    }
    if(!getline(file,line)){
        // what does getLine do 
        throw runtime_error("Empty_CSV");
    }
    vector<string> headers = parseCSVLine(line);

    // while(getline(file,line)){
    //     // what does getline do ?---> 
    //     stringstream ss(line);
    //     string column;

    //     while(getline(ss,column,',')){
    //         row.push_back(column);
    //     }
        
    // }
    // file.close();
    return row;
}

int main(){

    vector<string> dataRow = readCsv();
    // cout<<dataRow[200]<<endl;
    return 0;
}