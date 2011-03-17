#include "itkImage.h"
#include "itkVector.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkExtractImageFilter.h"

#include <sstream>

int main( int argc, char* argv[] )
{
  if( argc < 3 )
    {
    std::cerr << "usage: " << argv[0];
    std::cerr << " displacementImage.mha frameNum outputDisplacementImage.mha" << std::endl;
    return 1;
    }

  typedef double PixelType;
  const unsigned int InputDimension = 3;
  const unsigned int OutputDimension = 2;
  const unsigned int Components = 2;

  typedef itk::Image< itk::Vector< PixelType, Components >, InputDimension > InputImageType;
  typedef itk::Image< itk::Vector< PixelType, Components >, OutputDimension > OutputImageType;

  typedef itk::ImageFileReader< InputImageType > ReaderType;
  ReaderType::Pointer reader = ReaderType::New();
  reader->SetFileName( argv[1] );
  reader->UpdateOutputInformation();

  typedef itk::ExtractImageFilter< InputImageType, OutputImageType > ExtractorType;
  ExtractorType::Pointer extractor = ExtractorType::New();
  extractor->SetInput( reader->GetOutput() );

  typedef InputImageType::RegionType RegionType;
  RegionType::SizeType size = reader->GetOutput()->GetLargestPossibleRegion().GetSize();
  RegionType::IndexType index = reader->GetOutput()->GetLargestPossibleRegion().GetIndex();
  size[2] = 0;

  std::istringstream istrm( argv[2] );
  istrm >> index[2];

  RegionType region;
  region.SetSize( size );
  region.SetIndex( index );
  extractor->SetExtractionRegion( region );

  typedef itk::ImageFileWriter< OutputImageType > WriterType;
  WriterType::Pointer writer = WriterType::New();
  writer->SetFileName( argv[3] );
  writer->SetInput( extractor->GetOutput() );

  try
    {
    writer->Update();
    }
  catch( itk::ExceptionObject & err )
    {
    std::cerr << "ExceptionObject caught !" << std::endl;
    std::cerr << err << std::endl;
    return 1;
    }
  return 0;
}
